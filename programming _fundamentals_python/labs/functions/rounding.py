def rounding_nums(nums):
    nums = [round(float(num)) for num in nums]
    return nums


current_numbers = input().split()

print(rounding_nums(current_numbers))
