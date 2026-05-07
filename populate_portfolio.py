from generator import generate_ideas
from automation import scaffold_business
from website_gen import generate_showcase_html
from tester import run_tests
import os

def populate():
    print("🎨 Populating Portfolio with new ventures...")
    ideas = generate_ideas()
    
    for idea in ideas:
        print(f"\nProcessing: {idea['name']}")
        path = scaffold_business(idea)
        
        # Test it
        if run_tests(path):
            print(f"✅ {idea['name']} passed tests.")
        else:
            print(f"⚠️ {idea['name']} failed tests, but keeping in scaffold.")

    # Update the website
    showcase_path = generate_showcase_html()
    print(f"\n✨ Portfolio website updated! View it at {showcase_path}")

if __name__ == "__main__":
    populate()
