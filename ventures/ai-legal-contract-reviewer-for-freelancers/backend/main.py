
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"business": "AI Legal Contract Reviewer for Freelancers", "status": "active", "metrics": "optimized"}

@app.get("/process-call")
def process_call():
    responses = ["Booking appointment...", "Answering FAQ...", "Routing to human..."]
    return {"ai_response": random.choice(responses)}

if __name__ == "__main__":
    import uvicorn
    print("Launching AI Legal Contract Reviewer for Freelancers Backend...")
    # uvicorn.run(app, host="0.0.0.0", port=8000)
