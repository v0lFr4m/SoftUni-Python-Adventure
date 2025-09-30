number_of_usernames = int(input())

unique_usernames = set()

for name in range(number_of_usernames):
    unique_usernames.add(input())

for name in unique_usernames:
    print(name)