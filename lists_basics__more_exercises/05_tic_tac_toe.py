first_board_lines = input().split()
second_board_lines = input().split()
third_board_lines = input().split()
have_winner = False
whole_board = first_board_lines + second_board_lines + third_board_lines
position_counter = 0
step_index = 0

while position_counter <= 2 and not have_winner:
    winner_line = []
    # first check consecutive positions 0,1,2 - 3,4,5 - 6,7,8
    for h in range(position_counter * 3, (position_counter * 3) + 3):
        winner_line.append(whole_board[h])

    if winner_line.count("1") == 3:
        have_winner = True
        print("First player won")
        break
    elif winner_line.count("2") == 3:
        have_winner = True
        print("Second player won")
        break

    winner_line = []
    # second, check consecutive positions 0,3,6 - 1,4,7 - 2,5,8
    for v in range(position_counter, len(whole_board) + 1, 3):
        if len(winner_line) < 3:
            winner_line.append(whole_board[v])
        else:
            pass

    if winner_line.count("1") == 3:
        have_winner = True
        print("First player won")
        break
    elif winner_line.count("2") == 3:
        have_winner = True
        print("Second player won")
        break

    winner_line = []
    # second, check consecutive positions 0,4,8 - 2,4,6
    if position_counter < 2:
        for d in range(position_counter + position_counter, len(whole_board) + 1, 4 - (position_counter * 2)):
            if len(winner_line) < 3:
                winner_line.append(whole_board[d])
            else:
                pass

        if winner_line.count("1") == 3:
            have_winner = True
            print("First player won")
            break
        elif winner_line.count("2") == 3:
            have_winner = True
            print("Second player won")
            break

    position_counter += 1

if not have_winner:
    print("Draw!")
