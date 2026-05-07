import time
import random
import json
import os

def check_profitability(app_name):
    # Simulate production database/Stripe check
    metrics = {
        "active_users": random.randint(100, 500),
        "monthly_recurring_revenue": random.uniform(500, 5000),
        "churn_rate": "2.4%"
    }
    print(f"[Monitor] {app_name} | MRR: ${metrics['monthly_recurring_revenue']:.2f} | Users: {metrics['active_users']}")
    return metrics

def run_monitor(venture_list):
    print("--- Business Monitor Active ---")
    while True:
        for venture in venture_list:
            m = check_profitability(venture['name'])
            if m['monthly_recurring_revenue'] > 4000:
                print(f"!!! {venture['name']} is highly profitable. Triggering Exit Sequence...")
                return venture, m
        time.sleep(2) # Fast simulation speed

if __name__ == "__main__":
    run_monitor([{"name": "LocalBiz AI Voice Receptionist"}])
