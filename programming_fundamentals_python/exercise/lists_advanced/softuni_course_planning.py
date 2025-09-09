def add_lesson(courses_list :list , title_ :str) -> list:
    if title_ not in courses_list:
        courses_list.append(title_)
    return courses_list

def insert_lesson(courses_list: list, title_: str, index_: int) -> list:
    if title_ not in courses_list:
        if 0 <= index_ <= len(courses_list):
            courses_list.insert(index_, title_)
    return courses_list

def remove_lesson(courses_list :list , title_ :str) -> list:
    exercise = f"{title_}-Exercise"

    if title_ in courses_list:
        courses_list.remove(title_)

    if exercise in courses_list:
        courses_list.remove(exercise)

    return courses_list


def swap_lessons(courses_list: list, first_title: str, second_title: str) -> list:
    if first_title in courses_list and second_title in courses_list:
        first_exercise = f"{first_title}-Exercise"
        second_exercise = f"{second_title}-Exercise"
        first_index = courses_list.index(first_title)
        second_index = courses_list.index(second_title)

        courses_list[first_index], courses_list[second_index] = courses_list[second_index], courses_list[first_index]


        if first_exercise in courses_list:
            courses_list.remove(first_exercise)
            courses_list.insert(second_index + 1, first_exercise)
        if second_exercise in courses_list:
            courses_list.remove(second_exercise)
            courses_list.insert(first_index + 1, second_exercise)

    return courses_list


def add_exercise(courses_list: list, title_: str) -> list:
    exercise = f"{title_}-Exercise"
    if title_ in courses_list:
        if exercise not in courses_list:
            lesson_index = courses_list.index(title_)
            courses_list.insert(lesson_index + 1, exercise)
    else:
        courses_list.append(title_)
        courses_list.append(exercise)
    return courses_list


courses = input().split(", ")
COMMAND = False

while not COMMAND:
    current_command = input().split(':')
    if current_command[0] == "course start":
        COMMAND = True

    if current_command[0] == 'Add':
        title = current_command[1]
        add_lesson(courses , title)

    elif current_command[0] == 'Insert':
        title = current_command[1]
        index = int(current_command[2])
        insert_lesson(courses , title , index)

    elif current_command[0] == 'Remove':
        title = current_command[1]
        remove_lesson(courses , title)

    elif current_command[0] == 'Swap':
        first = current_command[1]
        second = current_command[2]
        swap_lessons(courses , first , second)

    elif current_command[0] == 'Exercise':
        title = current_command[1]
        add_exercise(courses , title)

for lesson_index, lesson_title in enumerate(courses, start=1):
    print(f"{lesson_index}.{lesson_title}")