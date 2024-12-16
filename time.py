import time

timestamp_hour = int(time.strftime('%H'))
print(timestamp_hour)

if 0 <= timestamp_hour < 12:
    print("Good morning!")
else:
    print("good night")
