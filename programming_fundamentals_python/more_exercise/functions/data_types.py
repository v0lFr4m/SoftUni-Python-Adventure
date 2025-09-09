def data_type(some_type :str , some_text: str):
    if some_type == 'int':    # If the data type is an int, multiply the number by 2
        return int(some_text) * 2
    elif some_type == 'real':  # If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
        return f"{float(some_text) * 1.5:.2f}"
    elif some_type == 'string': # If the data type is a string, surround the input with "$".
        return f"${some_text}$"




# INPUT
current_type = input()
text = input()
print(data_type(current_type , text))