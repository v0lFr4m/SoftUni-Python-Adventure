import math
from math import floor

centuries = int(input())

years = centuries * 100
days = floor(years * 365.2422)
hours = floor(days * 24)
minutes = floor(hours * 60)

print(f"{centuries} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")