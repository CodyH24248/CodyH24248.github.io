def generate_legal_docs(venture_name):
    print(f"Generating legal boilerplate for {venture_name}...")
    
    privacy_policy = f"""
# Privacy Policy for {venture_name}
We value your privacy. We collect:
1. Contact info (phone, email)
2. Voice recording data (to improve AI accuracy)
3. Calendar access (for booking)

Data is encrypted and never sold to third parties.
"""

    tos = f"""
# Terms of Service for {venture_name}
1. Service: We provide an automated AI voice receptionist.
2. Responsibility: You are responsible for ensuring AI interactions comply with local telemarketing laws.
3. Billing: Subscriptions are billed monthly.
"""
    return {"privacy_policy": privacy_policy, "tos": tos}

if __name__ == "__main__":
    docs = generate_legal_docs("LocalBiz AI Voice Receptionist")
    print("Legal docs generated.")
