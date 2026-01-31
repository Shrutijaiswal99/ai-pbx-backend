# AI PBX Backend – FastAPI

## Project Description
This project is a FastAPI-based backend that ingests call packets, stores them in a database, and simulates transcription processing.

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## API Endpoint
POST /v1/call/stream/{call_id}

### Request Body (JSON)
```json
{
  "sequence": 1,
  "data": "hello audio",
  "timestamp": 123.45
}



