start = int(input())
end = int(input())
char = ""
for i in range(start , end + 1):
    char += chr(i) + " "
print(char)