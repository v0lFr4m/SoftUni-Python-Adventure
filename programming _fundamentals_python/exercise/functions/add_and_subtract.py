
def sum_of_num(first:int , second:int):
    return first + second
def subtrack(result:int, third:int) -> int:
    return result - third
def add_and_subtrack(first: int, second: int, third: int):
    sum_of_numbers = sum_of_num(first , second)
    subtracted = subtrack(sum_of_numbers , third)
    return subtracted



current_first_num = int(input())
current_second_num = int(input())
current_third_num = int(input())

print(add_and_subtrack(current_first_num , current_second_num , current_third_num))