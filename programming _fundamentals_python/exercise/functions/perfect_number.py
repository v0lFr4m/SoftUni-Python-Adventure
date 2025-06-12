def perfect_num(num:int):
    divisors = sum([i for i in range(1, num) if num % i == 0])

    if num == divisors:
        return "We have a perfect number!"
    else:
        return  "It's not so perfect."



number = int(input())

print(perfect_num(number))
