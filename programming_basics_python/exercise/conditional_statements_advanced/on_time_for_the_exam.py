exam_hour = int(input())
exam_minute = int(input())
student_hour = int(input())
student_minute = int(input())

exam_minutes = exam_hour * 60 + exam_minute
studentMinutes = student_hour * 60 + student_minute

difference = exam_minutes - studentMinutes

minutes = abs(difference) % 60
if minutes < 10 and abs(difference) >= 60:
    minutes = f"0{minutes}"

hours = abs(difference) // 60

if 0 <= difference <= 30:
    print("On time")
    if difference != 0:
        print(f"{minutes} minutes before the start")
elif 30 < difference < 60:
    print("Early")
    print(f"{minutes} minutes before the start")
elif 60 <= difference:
    print("Early")
    print(f"{hours}:{minutes} hours before the start")
elif 0 > difference > -60:
    print("Late")
    print(f"{minutes} minutes after the start")
elif -60 >= difference:
    print("Late")
    print(f"{hours}:{minutes} hours after the start")