pages = int(input())
pages_per_hour = int(input())
days_need_to_read = int(input())


needed_hours_per_day = (pages / pages_per_hour) / days_need_to_read

print(f"{needed_hours_per_day:.0f}")
