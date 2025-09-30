number_of_guest = int(input())
guest_list = set()
for _ in range(number_of_guest):
    guest_list.add(input())

while (reservation := input()) != 'END':
    if reservation in guest_list:
        guest_list.remove(reservation)

print(len(guest_list))
sorted_reservations = sorted(guest_list)

for reservation in sorted_reservations:
    print(reservation)