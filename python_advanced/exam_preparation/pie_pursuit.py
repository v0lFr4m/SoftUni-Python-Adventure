from collections import deque

contestants = deque(map(int,input().split()))
pies = list(map(int, input().split()))

while contestants and pies:
    first_contestant = contestants.popleft()
    last_pie = pies.pop()

    if first_contestant >= last_pie:
        first_contestant -= last_pie

        if first_contestant > 0:
            contestants.append(first_contestant)

    else:
        last_pie -= first_contestant
        if last_pie == 1 and pies:
            pies[-1] += last_pie
        else:
            pies.append(last_pie)

if contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(i) for i in contestants)}")
elif pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(i) for i in pies)}")
else:
    print("We have a champion!")
