from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import asyncio
import logging

from app.database import engine, get_db
from app.models import Base, Call, Packet
from app.schemas import PacketIn
from app.tasks import process_ai_with_retry

logging.basicConfig(level=logging.WARNING)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/v1/call/stream/{call_id}", status_code=202)
async def ingest_packet(
    call_id: str,
    packet: PacketIn,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Call).where(Call.id == call_id))
    call = result.scalar_one_or_none()

    if not call:
        call = Call(id=call_id)
        db.add(call)
        await db.commit()
        await db.refresh(call)

    # Validate packet sequence
    if packet.sequence != call.last_sequence + 1:
        logging.warning(f"Packet missing for call {call_id}")

    call.last_sequence = packet.sequence

    new_packet = Packet(
        call_id=call_id,
        sequence=packet.sequence,
        data=packet.data,
        timestamp=packet.timestamp
    )

    db.add(new_packet)
    await db.commit()

    # Non-blocking AI processing
    asyncio.create_task(process_ai_with_retry(call_id))

    return {"message": "Packet accepted"}
