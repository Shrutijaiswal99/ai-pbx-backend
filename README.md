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
```
### Successful API Execution (Logs)
```text
INFO sqlalchemy.engine.Engine SELECT calls.id, calls.state, calls.last_sequence
FROM calls
WHERE calls.id = ?
INFO sqlalchemy.engine.Engine INSERT INTO packets (call_id, sequence, data, timestamp)
VALUES (?, ?, ?, ?)
INFO sqlalchemy.engine.Engine COMMIT
INFO: 127.0.0.1:59958 "POST /v1/call/stream/test123 HTTP/1.1" 202 Accepted
[SUCCESS] Call test123: Transcription successful


