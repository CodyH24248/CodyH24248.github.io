def generate_ads(venture_name, description):
    print(f"Generating ad copy for {venture_name}...")
    ads = {
        "Facebook": f"Tired of missing customer calls? {venture_name} is your 24/7 AI receptionist. {description} Start your free trial today!",
        "Google_Search": f"{venture_name} - AI Voice Booking for Small Biz. Never miss a lead again. Automated appointment scheduling.",
        "LinkedIn": f"Scale your local service business with {venture_name}. Our AI agents handle the phone so you can handle the job. #AI #SmallBiz #Automation"
    }
    return ads

if __name__ == "__main__":
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "LocalBiz AI Voice Receptionist"
    desc = "AI voice agents for local trades."
    print(generate_ads(name, desc))
