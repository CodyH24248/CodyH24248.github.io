import time
from launch import launch_and_manage

def start_continuous_earning():
    print("💰 CONTINUOUS EARNING MODE ACTIVATED")
    print("The system will now build, scale, and sell ventures in a loop.")
    
    cycle_count = 1
    while True:
        print(f"\n--- STARTING CYCLE #{cycle_count} ---")
        try:
            launch_and_manage()
            print(f"--- COMPLETED CYCLE #{cycle_count} ---")
            cycle_count += 1
            print("Taking a short break before the next venture...")
            time.sleep(10) # Pause between ventures
        except Exception as e:
            print(f"Error in cycle: {e}")
            time.sleep(60) # Wait longer on error

if __name__ == "__main__":
    start_continuous_earning()
