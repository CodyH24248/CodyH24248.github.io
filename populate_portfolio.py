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
    import subprocess
    base_dir = "/home/engine/automated-ventures"
    try:
        subprocess.run(["cp", f"{base_dir}/showcase.html", f"{base_dir}/index.html"], check=True)
        subprocess.run(["git", "-C", base_dir, "add", "."], check=True)
        subprocess.run(["git", "-C", base_dir, "commit", "-m", "Bulk update portfolio"], check=True)
        subprocess.run(["git", "-C", base_dir, "push", "origin", "main"], check=True)
        print(f"\n✨ Portfolio website updated and pushed! View it at https://CodyH24248.github.io/VentureMachine")
    except Exception as e:
        print(f"⚠️  Failed to push updates: {e}")

if __name__ == "__main__":
    populate()
