# Write a program that traverses a given directory for all files.
# Search through to the first nested level of the directory (inclusive) and ,
# write information about each file you find into the report.txt file.
# The files should be grouped by their extension.
# Extensions should be ordered alphabetically by name. The files with extensions should also be sorted by name.
# The report.txt file should be saved in the chosen directory.


import os
files = {}
directory = "../"

for element in os.listdir(directory):
    file = os.path.join(directory , element)
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(file):
            filename = os.path.join(file , el)
            if os.path.isfile(filename):
                ext = os.path.splitext(filename)[1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)
with open('report.txt', 'w') as report:
    for ext, filenames in sorted(files.items()):
        report.write(f'{ext}\n')
        for name in sorted(filenames):
            report.write(f'- - - {name}\n')