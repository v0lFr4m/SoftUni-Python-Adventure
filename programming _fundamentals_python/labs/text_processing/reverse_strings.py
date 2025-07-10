
while (text := input()) != 'end':
    text_reversed = ''
    for char in reversed(text):
        text_reversed += char
    print(f"{text} = {text_reversed}")