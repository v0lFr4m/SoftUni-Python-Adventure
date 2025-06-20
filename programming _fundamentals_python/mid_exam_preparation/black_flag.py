days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

gained_plunder = 0
for day in range(1 , days + 1):
    gained_plunder += daily_plunder

    if day % 3 == 0:
        gained_plunder +=daily_plunder * 0.5

    if day % 5 == 0:
        gained_plunder -= (gained_plunder * 0.3)

if gained_plunder >= expected_plunder:
    print(f"Ahoy! {gained_plunder:.2f} plunder gained.")
elif gained_plunder < expected_plunder:
    percentage = (gained_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
