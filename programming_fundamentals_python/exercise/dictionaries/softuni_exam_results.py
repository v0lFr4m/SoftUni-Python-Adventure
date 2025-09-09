users = {}
languages = {}

while (line := input()) != "exam finished":

    if "banned" in line:
        username = line.split("-")[0]
        if username in users:
            del users[username]
    else:
        username, language, points = line.split("-")
        points = int(points)

        if language not in languages:
            languages[language] = 0
        languages[language] += 1

        if username not in users:
            users[username] = points
        else:
            if points > users[username]:
                users[username] = points

print("Results:")
for username, points in users.items():
    print(f"{username} | {points}")

print("Submissions:")
for language, count in languages.items():
    print(f"{language} - {count}")