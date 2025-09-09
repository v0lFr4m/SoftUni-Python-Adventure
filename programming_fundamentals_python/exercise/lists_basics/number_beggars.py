START_INDEX = 0
money_as_string = input().split(", ")
number_of_beggars = int(input())
final_list = []

money_as_int = [int(money) for money in money_as_string]
#for current_money in money_as_string:
#    money_as_int.append((int(current_money)))

for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(START_INDEX , len(money_as_int) , number_of_beggars):
        current_beggar_sum += money_as_int[index]
    final_list.append(current_beggar_sum)
    START_INDEX += 1
print(final_list)