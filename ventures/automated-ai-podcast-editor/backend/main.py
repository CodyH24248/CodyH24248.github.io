
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"business": "Automated AI Podcast Editor", "status": "active", "metrics": "optimized"}

@app.get("/process-call")
def process_call():
    responses = ["Booking appointment...", "Answering FAQ...", "Routing to human..."]
    return {"ai_response": random.choice(responses)}

if __name__ == "__main__":
    import uvicorn
    print("Launching Automated AI Podcast Editor Backend...")
    # uvicorn.run(app, host="0.0.0.0", port=8000)
