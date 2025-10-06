from collections import deque
price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
intelligence = int(input())

count_bullet = len(bullets)
counter_bullet = 0

while True:
    if len(bullets) == 0 or len(locks) == 0:
        break

    bullet = bullets[-1]
    lock = locks[0]

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    bullets.pop()
    counter_bullet += 1
    if counter_bullet == gun_barrel_size and len(bullets) != 0:
        counter_bullet = 0
        print("Reloading!")

count_bullet -= len(bullets)
bullets_cost = count_bullet * price_of_bullet

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")