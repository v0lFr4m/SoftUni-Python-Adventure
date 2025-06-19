targets = list(map(int,input().split()))
command = input()
shot_targets = 0
last_target = 0
empty_list = []
while command != "End":
    current_shot = int(command)
    if current_shot < len(targets):
        last_target = targets[current_shot]
        for target_index in range(len(targets)):
            current_target_value = targets[target_index]
            if current_shot == target_index:

                targets[target_index] = -1
                shot_targets += 1
            if current_target_value > last_target and targets[target_index] != -1:
                targets[target_index] -= last_target

            if current_target_value <= last_target and targets[target_index] != -1:
                targets[target_index] += last_target
    else:
        command = input()
        continue
    command = input()


print(f"Shot targets: {shot_targets} -> {' '.join(str(i) for i in targets)}")