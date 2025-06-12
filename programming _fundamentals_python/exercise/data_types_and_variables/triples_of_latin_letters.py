
n = int(input())
letters = [chr(ord('a') + i) for i in range(n)]

for i in letters:
    for j in letters:
        for k in letters:
            print(i + j + k)

