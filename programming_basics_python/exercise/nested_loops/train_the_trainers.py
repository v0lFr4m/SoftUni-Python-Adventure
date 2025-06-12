judges_count = int(input())
command = input()

total_avg_sum = 0
total_presentations_count = 0

while command != 'Finish':
    current_presentation = command

    current_score = 0
    for _ in range(judges_count):
        judge_score = float(input())
        current_score += judge_score

    current_score_avg = current_score / judges_count

    print(f'{current_presentation} - {current_score_avg:.2f}.')

    total_avg_sum += current_score_avg
    total_presentations_count += 1

    command = input()

total_avg = total_avg_sum / total_presentations_count
print(f'Student\'s final assessment is {total_avg:.2f}.')