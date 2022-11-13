# dollars_string = input()
# people = input()
#
# dollars = []
# dollars_sum_list = []
#
# for amount in dollars_string:
#     dollars.append(int(amount))
#
# index_people = 0
#
# while index_people < people:
#     taken_amount = 0
#     beggar_takes = []
#
#     for money in range(index_people, len(dollars), people):
#         taken_amount = dollars[money]
#         beggar_takes.append(taken_amount)
#
#     dollars_sum_list.append(sum(beggar_takes))
#     index_people += 1
#
# print(dollars_sum_list)


dollars_string = input().split(", ")
people = int(input())
dollars = []
dollars_sum_list = []

for amount in dollars_string:
    dollars.append(int(amount))

index_people = 0

while index_people < people:
    taken_amount = 0
    beggar_takes = []

    for money in range(index_people, len(dollars), people):
        taken_amount = dollars[money]
        beggar_takes.append(taken_amount)

    dollars_sum_list.append(sum(beggar_takes))
    index_people += 1

print(dollars_sum_list)
