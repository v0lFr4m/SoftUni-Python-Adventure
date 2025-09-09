number_of_lines = int(input())
brackets = []

for i in range(number_of_lines):
    text = input()

    if text == "(":
        # Проверяваме за последователност на отворените скоби
        if brackets and brackets[-1] == "(":
            # Ако имаме две последователни отворени скоби
            print("UNBALANCED")
            exit()  # Прекратяваме програмата, тъй като изразът е невалиден
        brackets.append(text)  # Добавяме отворената скоба

    elif text == ")":
        # Проверка преди добавяне на затворена скоба
        if not brackets or brackets[-1] != "(":
            print("UNBALANCED")
            exit()  # Прекратяваме, ако няма отворена скоба за затваряне
        brackets.pop()  # Изваждаме последната добавена отворена скоба

# Проверка след цикъла
if not brackets:
    print("BALANCED")
else:
    print("UNBALANCED")