numbers = sorted(list(map(int , input().split())), reverse=True)

average = sum(numbers) / len(numbers)
total = []
for num in numbers:
    if len(numbers) != 1:
        if num > average:
            if len(total) <= 4:
                total.append(num)
                        
if len(total) != 0:
    print(f" ".join(str(i) for i in total))
else:
    print('No')

