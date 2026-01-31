import random
import asyncio

async def fake_ai_transcription():
    await asyncio.sleep(random.randint(1, 3))

    if random.random() < 0.25:
        raise Exception("AI Service Unavailable")

    return "Transcription successful"
