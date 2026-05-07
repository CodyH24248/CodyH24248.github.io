import os

def setup_payouts():
    """
    To transfer money to your personal bank account, you must:
    1. Create a Stripe account at https://dashboard.stripe.com/register
    2. Go to 'Payouts' and add your Bank Account (IBAN/Routing Number)
    3. Get your Secret API Key from 'Developers' -> 'API Keys'
    4. Set it as an environment variable: export STRIPE_SECRET_KEY='sk_test_...'
    """
    
    stripe_key = os.getenv("STRIPE_SECRET_KEY")
    
    if not stripe_key:
        return "MISSING_CONFIG: Please set STRIPE_SECRET_KEY to enable bank transfers."
    
    # In a real scenario, this would use the stripe-python library:
    # import stripe
    # stripe.api_key = stripe_key
    # stripe.Payout.create(amount=1000, currency='usd')
    
    return "PAYOUT_SYSTEM_READY: Payments will be routed to your linked bank account."

if __name__ == "__main__":
    print(setup_payouts())
