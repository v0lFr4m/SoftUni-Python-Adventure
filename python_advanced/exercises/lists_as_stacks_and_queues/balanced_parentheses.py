expression = input()
brackets_stack = []

parenthesis = {'(':")",'{':"}", '[':"]"}

for char in expression:
    if char in parenthesis:
        brackets_stack.append(char)
    elif char in parenthesis.values():
        if not brackets_stack:
            print("NO")
            break
        last_open_bracket = brackets_stack.pop()
        if parenthesis[last_open_bracket] != char:
            print("NO")
            break
else:
    if not brackets_stack:
        print("YES")
    else:
        print("NO")




