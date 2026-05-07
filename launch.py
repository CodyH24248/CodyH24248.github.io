from generator import generate_ideas
from research import research_idea
from automation import scaffold_business
from monitor import run_monitor
from seller import list_for_sale
from advertising import generate_ads
from legal import generate_legal_docs
from payments import setup_payouts
from tester import run_tests
from website_gen import generate_showcase_html

def launch_and_manage():
    print("\n🚀 STARTING FULLY COMPLIANT VENTURE PIPELINE\n" + "="*40)
    
    # 1. Ideation
    ideas = generate_ideas()
    selected = ideas[0]
    print(f"✔️  Target identified: {selected['name']}")

    # 2. Market Validation & Legal Prep
    research_idea(selected['name'])
    docs = generate_legal_docs(selected['name'])
    print(f"✔️  Market validated and Legal Docs generated.")

    # 3. Build & Scaffolding
    path = scaffold_business(selected)
    print(f"✔️  Business logic deployed to {path}")

    # 4. Testing Phase
    test_passed = run_tests(path)
    if not test_passed:
        print("❌ Venture failed quality testing. Aborting launch.")
        return

    # 5. Payout Config & Marketing
    payout_status = setup_payouts()
    print(f"✔️  Payment System: {payout_status}")
    ads = generate_ads(selected['name'], selected['description'])
    print(f"✔️  Ad copy ready for distribution.")

    # 6. Website Update
    generate_showcase_html()
    print(f"✔️  Portfolio website updated with new venture.")

    # 7. Monitoring & Growth (Simulation)
    print("\n📈 MOVING TO MONITORING PHASE...")
    sold_venture, final_metrics = run_monitor([selected])

    # 8. Automated Marketplace Posting
    print("\n💰 REVENUE TARGET MET. POSTING TO MARKETPLACE...")
    list_for_sale(sold_venture['name'], final_metrics)
    
    print("\n" + "="*40 + "\n🏁 EXIT COMPLETE. VENTURE POSTED & READY FOR TRANSFER.")

if __name__ == "__main__":
    launch_and_manage()
