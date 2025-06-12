time = int(input())
day_of_week = input()

open_close = ""

if 10 <= time <= 18:
    if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" or day_of_week == "Thursday" or day_of_week == "Friday" or day_of_week == "Saturday":
        open_close += "open"
    else:
        open_close += "closed"
else:
    open_close += "closed"
print(open_close)