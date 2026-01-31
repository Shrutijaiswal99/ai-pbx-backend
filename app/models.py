from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

class CallState(enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    PROCESSING_AI = "PROCESSING_AI"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    ARCHIVED = "ARCHIVED"

class Call(Base):
    __tablename__ = "calls"

    id = Column(String, primary_key=True, index=True)
    state = Column(Enum(CallState), default=CallState.IN_PROGRESS)
    last_sequence = Column(Integer, default=0)

    packets = relationship("Packet", back_populates="call")

class Packet(Base):
    __tablename__ = "packets"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, ForeignKey("calls.id"))
    sequence = Column(Integer)
    data = Column(String)
    timestamp = Column(Float)

    call = relationship("Call", back_populates="packets")
