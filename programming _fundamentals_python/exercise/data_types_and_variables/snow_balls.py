n = int(input())
best_value = 0

current_weight = 0
current_time = 0
current_quality = 0

for snowball in range(1 , n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snow_ball_value = (weight / time) ** quality

    if snow_ball_value > best_value:
        best_value = snow_ball_value
        current_weight = weight
        current_time = time
        current_quality = quality

print(f"{current_weight} : {current_time} = {best_value:.0f} ({current_quality})")

