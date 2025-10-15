from collections import deque

required_strength = list(map(int,input().split()))
accuracy = deque(map(int, input().split()))
scored_goals = 0
while required_strength and accuracy:
    strength_element = required_strength[-1]
    accuracy_element = accuracy[0]
    sum_of_elements = strength_element + accuracy_element

    if sum_of_elements == 100:
        required_strength.pop()
        accuracy.popleft()
        scored_goals += 1

    elif sum_of_elements < 100:
        if strength_element < accuracy_element:
            required_strength.pop()

        elif strength_element > accuracy_element:
            accuracy.popleft()

        elif strength_element == accuracy_element:

            sum_of_elements = strength_element + accuracy_element
            required_strength.pop()
            required_strength.append(sum_of_elements)
            accuracy.popleft()

    elif sum_of_elements > 100:
        index_of_strength_element = required_strength.index(strength_element)
        required_strength[index_of_strength_element] -= 10
        accuracy.popleft()
        accuracy.append(accuracy_element)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")
if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")
if required_strength:
    print(f"Strength values left: {', '.join(str(el) for el in required_strength)}")
elif accuracy:
    print(f"Accuracy values left: {', '.join(str(el) for el in accuracy)}")


