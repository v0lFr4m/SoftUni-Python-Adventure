MONTHS = 12

deposit_sum = float(input())
term_in_month = int(input())
annual_interest_rate = float(input())

total_sum = deposit_sum + term_in_month * ((deposit_sum * (annual_interest_rate/100)) / MONTHS)
print(total_sum)