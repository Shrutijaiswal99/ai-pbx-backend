import asyncio
from app.ai_mock import fake_ai_transcription

async def process_ai_with_retry(call_id: str, max_retries: int = 5):
    for attempt in range(max_retries):
        try:
            result = await fake_ai_transcription()
            print(f"[SUCCESS] Call {call_id}: {result}")
            return
        except Exception as e:
            wait_time = 2 ** attempt
            print(f"[RETRY] Call {call_id} attempt {attempt+1}, waiting {wait_time}s")
            await asyncio.sleep(wait_time)

    print(f"[FAILED] AI processing failed for call {call_id}")
