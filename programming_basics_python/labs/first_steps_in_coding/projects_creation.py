HOURS_PER_PROJECT = 3

architect = input()
number_of_project = int(input())

needed_hours = number_of_project * HOURS_PER_PROJECT

print(f"The architect {architect} will need {needed_hours} hours to complete {number_of_project} project/s.")