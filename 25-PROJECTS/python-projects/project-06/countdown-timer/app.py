import time

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)  # Converts seconds into minutes and seconds
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')  # Print the time in place to update it
        time.sleep(1)  # Pause the program for 1 second
        t -= 1  # Decrease the time by 1 second
    print("00:00")  # Print 00:00 when the countdown is finished

# Get user input for countdown time
time_in_seconds = int(input("Enter the time in seconds: "))
countdown(time_in_seconds)
