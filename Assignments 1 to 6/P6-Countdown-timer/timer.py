import time
from datetime import datetime, timedelta

# Simple countdown timer without classes
def countdown_timer():
    try:
        # Ask user for countdown duration
        duration_input = input("Enter countdown time in format HH:MM:SS: ")
        hours, minutes, seconds = map(int, duration_input.split(':'))
    except ValueError:
        print("Invalid format. Please use HH:MM:SS.")
        return

    # Calculate end time
    now = datetime.now()
    delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    end_time = now + delta
    print(f"\nCountdown started for {hours}h {minutes}m {seconds}s.\n")

    # Loop until time is up
    while True:
        remaining = end_time - datetime.now()
        if remaining.total_seconds() <= 0:
            print("Time's up!")
            break

        # Format remaining time as HH:MM:SS
        rem_h, rem_r = divmod(int(remaining.total_seconds()), 3600)
        rem_m, rem_s = divmod(rem_r, 60)
        timer_display = f"{rem_h:02d}:{rem_m:02d}:{rem_s:02d}"
        print(f"Remaining: {timer_display}", end='\r')
        time.sleep(1)

if __name__ == '__main__':
    countdown_timer()