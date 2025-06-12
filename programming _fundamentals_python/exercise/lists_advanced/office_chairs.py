number_of_rooms = int(input())
total_chairs = 0
total_visitors = 0
for room in range(1 ,number_of_rooms + 1):
    chairs_information = input().split()
    chairs = len(chairs_information[0])
    visitors = int(chairs_information[1])
    total_chairs += chairs
    if chairs < visitors:
        needed_chairs = abs(visitors - chairs)
        total_chairs -= visitors
        print(f"{needed_chairs} more chairs needed in room {room}")
    else:
        total_chairs -=visitors
if total_chairs >= 0:
    print(f"Game On, {total_chairs} free chairs left")