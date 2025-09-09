def repeat_string(string):
    new_string = ''
    for char in range(counter):
      new_string += string
    return new_string


input_string = input()
counter = int(input())

print(repeat_string(input_string))