COUNT_POSITIVES = []
SUM_OF_NEGATIVE = []

n = int(input())

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        COUNT_POSITIVES.append(current_number)
    else:
        SUM_OF_NEGATIVE.append(current_number)

print(COUNT_POSITIVES)
print(SUM_OF_NEGATIVE)
print(f"Count of positives: {len(COUNT_POSITIVES)}")
print(f"Sum of negatives: {sum(SUM_OF_NEGATIVE)}")
