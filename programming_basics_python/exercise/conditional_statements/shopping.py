GPU_PRICE = 250
CPU_PRICE = 0.35
RAM_PRICE = 0.10
DISCOUNT = 0.15

budget = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

gpu = number_of_gpu * GPU_PRICE
cpu = number_of_cpu * (gpu * CPU_PRICE)
ram = number_of_ram * (gpu * RAM_PRICE)
total_sum = gpu + cpu + ram
if number_of_gpu > number_of_cpu:
    total_sum = total_sum - (total_sum * DISCOUNT)
if budget >= total_sum:
    total_sum = abs(total_sum - budget)
    print(f"You have {total_sum:.2f} leva left!")
else:
    needed_sum = abs(total_sum - budget)
    print(f"Not enough money! You need {needed_sum:.2f} leva more!")