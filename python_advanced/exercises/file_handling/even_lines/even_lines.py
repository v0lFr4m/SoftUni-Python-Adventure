# Write a program that reads a text file and prints on the console its even lines.
# Line numbers start from 0.
# Before you print the result, replace {"-", ",", ".", "!", "?"} with "@"
# and reverse the order of the words.


with open('text.txt') as file:
    for index , line in enumerate(file):
        if index % 2 == 0:
            for char in {"-", ",", ".", "!", "?"} :
                line = line.replace(char , "@")
            print(' '.join(reversed(line.split(' '))))

