import math
RESISTENCE = 12.5
record = float(input())
current_range = float(input())
second_per_meter = float(input())

swimming_time = current_range * second_per_meter
total_range= math.floor((current_range / 15)) * RESISTENCE
total_time = swimming_time + total_range
if record <= total_time:
    needed_seconds = total_time - record
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")


