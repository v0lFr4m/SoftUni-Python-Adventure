import math

serial_name = input()
episode_duration = int(input())
rest_duration = int(input())

lunch_time = rest_duration / 8
rest_time = rest_duration / 4
time = rest_duration - lunch_time - rest_time

if time > episode_duration:
    time = abs(time - episode_duration)
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(time)} minutes free time.")
else:
    time = abs(time - episode_duration)
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(time)} more minutes.")