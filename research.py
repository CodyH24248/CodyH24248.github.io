import subprocess
import sys
import json

def research_idea(idea_name):
    print(f"Researching competition for: {idea_name}...")
    # Use agent-browser to search
    query = f"competitors for {idea_name} mobile app"
    # Note: In this environment, we'd trigger agent-browser via Bash
    cmd = ["agent-browser", "search", query]
    # This is a placeholder for the actual tool call
    return f"Search results for {query} would appear here."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        idea = sys.argv[1]
        print(research_idea(idea))
    else:
        print("Usage: python3 research.py <idea_name>")
