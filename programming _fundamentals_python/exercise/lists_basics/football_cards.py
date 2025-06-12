from queue import PriorityQueue

TEAM_A = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
TEAM_B = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
GAME_WAS_TERMINATED = False
players = input().split()
for player in players:
    if player in TEAM_A:
        TEAM_A.remove(player)

    elif player in TEAM_B:
        TEAM_B.remove(player)

    if len(TEAM_A) < 7 or len(TEAM_B) < 7:
        GAME_WAS_TERMINATED = True
        break

print(f"Team A - {len(TEAM_A)}; Team B - {len(TEAM_B)}")
if GAME_WAS_TERMINATED:
    print("Game was terminated")
