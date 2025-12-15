import time

print("⏰ Countdown Timer ⏰")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds
print("Starting countdown...\n")

for remaining in range(total_seconds, 0, -1):
    h, m = divmod(remaining, 3600)
    m, s = divmod(m, 60)
    print(f"{h:02}:{m:02}:{s:02}", end="\r")
    time.sleep(1)

print("\n💥 TIME’S UP!") 
