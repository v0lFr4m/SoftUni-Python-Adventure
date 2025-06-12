#input and split to correct value
first_line = input().split()
second_line = input().split()
third_line = input().split()
# Merger in one list
game_field = first_line + second_line + third_line

first_won = False
second_won = False

    # FIRST_PLAYER
# HORIZONTAL

if (game_field[0] == '1' and game_field[1] == '1' and game_field[2] == '1') or \
   (game_field[3] == '1' and game_field[4] == '1' and game_field[5] == '1') or \
   (game_field[6] == '1' and game_field[7] == '1' and game_field[8] == '1'):
    first_won = True
# VERTICALS

if (game_field[0] == '1' and game_field[3] == '1' and game_field[6] == '1') or \
   (game_field[1] == '1' and game_field[4] == '1' and game_field[7] == '1') or \
   (game_field[2] == '1' and game_field[5] == '1' and game_field[8] == '1'):
    first_won = True
# DIAGONALS

if (game_field[0] == '1' and game_field[4] == '1' and game_field[8] == '1') or \
     (game_field[2] == '1' and game_field[4] == '1' and game_field[6] == '1'):
    first_won = True

    # SECOND_PLAYER
# HORIZONTAL

if (game_field[0] == '2' and game_field[1] == '2' and game_field[2] == '2') or \
   (game_field[3] == '2' and game_field[4] == '2' and game_field[5] == '2') or \
   (game_field[6] == '2' and game_field[7] == '2' and game_field[8] == '2'):
    second_won = True
# VERTICALS

if (game_field[0] == '2' and game_field[3] == '2' and game_field[6] == '2') or \
   (game_field[1] == '2' and game_field[4] == '2' and game_field[7] == '2') or \
   (game_field[2] == '2' and game_field[5] == '2' and game_field[8] == '2'):
    second_won = True
# DIAGONALS

if (game_field[0] == '2' and game_field[4] == '2' and game_field[8] == '2') or \
   (game_field[2] == '2' and game_field[4] == '2' and game_field[6] == '2'):
    second_won = True

# Printing the result
if first_won:
    print("First player won")
elif second_won:
    print("Second player won")
else:
    print("Draw!")