sequence_of_nums = list(map(int , input().split()))

def separate(*args):
    negative_nums = []
    positive_nums = []

    nums = args[0]
    for num in nums:
        if num > 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)

    sum_negative = sum(negative_nums)
    sum_positive = sum(positive_nums)
    if abs(sum_negative) > sum_positive:
        return f"{sum_negative}\n{sum_positive}\nThe negatives are stronger than the positives"
    else:
        return f"{sum_negative}\n{sum_positive}\nThe positives are stronger than the negatives"

print(separate(sequence_of_nums))