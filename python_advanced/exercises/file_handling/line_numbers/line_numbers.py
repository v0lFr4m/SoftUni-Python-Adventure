from string import punctuation

# Write a program that reads a text file,
# inserts line numbers in front of each line,
# and counts all the letters and punctuation marks.
# The result should be written in another text file.

with open('text.txt') as input_file, open('output.txt','w') as output_file:
    result = []
    for index, line in enumerate(input_file):
        letters_counter = 0
        punctuation_marks_counter = 0
        for char in line:
            if char.isalpha():
                letters_counter += 1
            elif char in punctuation:
                punctuation_marks_counter += 1
        result.append(f'Line {index + 1}: {line.strip()} ({letters_counter})({punctuation_marks_counter})')
    output_file.write('\n'.join(result))


