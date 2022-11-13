a_team = ["A-" + str(i) for i in range(1, 12)]
b_team = ["B-" + str(i) for i in range(1, 12)]
# red_cards_list = red_cards.split(" ") #or red_cards_list = input().split(" ")
red_cards_list = input().split(" ")
is_terminated = False

for players in range(len(red_cards_list)):
    player = red_cards_list[players]
    if player in a_team:
        a_team.remove(player)
    elif player in b_team:
        b_team.remove(player)
    if len(a_team) < 7 or len(b_team) < 7:
        is_terminated = True
        break

print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if is_terminated:
    print("Game was terminated")
