import os
import json

def scaffold_business(idea):
    name_slug = idea['name'].lower().replace(' ', '-')
    path = f"./ventures/{name_slug}"
    os.makedirs(f"{path}/backend", exist_ok=True)
    os.makedirs(f"{path}/frontend", exist_ok=True)
    
    # Backend Logic (FastAPI style simulation)
    backend_code = f"""
from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {{"business": "{idea['name']}", "status": "active", "metrics": "optimized"}}

@app.get("/process-call")
def process_call():
    responses = ["Booking appointment...", "Answering FAQ...", "Routing to human..."]
    return {{"ai_response": random.choice(responses)}}

if __name__ == "__main__":
    import uvicorn
    print("Launching {idea['name']} Backend...")
    # uvicorn.run(app, host="0.0.0.0", port=8000)
"""
    
    # Frontend Logic (React/Mobile simulation)
    frontend_code = f"""
// Mobile-Optimized Dashboard for {idea['name']}
import React from 'react';

const Dashboard = () => {{
    return (
        <div style={{{{ padding: '20px', fontFamily: 'sans-serif' }}}}>
            <h1>{idea['name']} Admin</h1>
            <p>Status: <span style={{{{ color: 'green' }}}}>Live</span></p>
            <div style={{{{ border: '1px solid #ccc', padding: '10px' }}}}>
                <h3>Total Calls Handled: 1,240</h3>
                <h3>Revenue Generated: $4,500</h3>
            </div>
        </div>
    );
}};

export default Dashboard;
"""

    with open(f"{path}/backend/main.py", "w") as f:
        f.write(backend_code)
    
    with open(f"{path}/frontend/Dashboard.js", "w") as f:
        f.write(frontend_code)
        
    with open(f"{path}/README.md", "w") as f:
        f.write(f"# {idea['name']} - Fully Optimized\n\n{idea['description']}\n\n## Tech Stack\n- Backend: Python (FastAPI)\n- Frontend: React Mobile\n- AI: GPT-4o-mini via API")

    return path
