from pydantic import BaseModel

class PacketIn(BaseModel):
    sequence: int
    data: str
    timestamp: float
