import sys
import json
import time
from generator import generate_ideas
from research import research_idea
from automation import scaffold_business

class VentureAssistant:
    def __init__(self):
        print("--- Automated Venture Assistant Initialized ---")
        self.active_ventures = []

    def run_cycle(self):
        print("\n[Step 1] Generating new business ideas...")
        ideas = generate_ideas()
        
        # In a fully automated mode, we pick the one with highest automation potential
        best_idea = ideas[0] 
        print(f"Selected Idea: {best_idea['name']}")

        print(f"\n[Step 2] Conducting market research for: {best_idea['name']}...")
        research_results = research_idea(best_idea['name'])
        print(f"Research Findings: {research_results}")

        print(f"\n[Step 3] Scaffolding the business...")
        path = scaffold_business(best_idea)
        self.active_ventures.append({"idea": best_idea, "path": path})

        print(f"\n[Step 4] Handing over to Monitor...")
        print(f"Assistant is now monitoring {len(self.active_ventures)} ventures for profitability.")
        
        print("\n--- Cycle Complete. Business is live (simulated). ---")

if __name__ == "__main__":
    assistant = VentureAssistant()
    try:
        assistant.run_cycle()
    except KeyboardInterrupt:
        print("\nAssistant shutting down.")
