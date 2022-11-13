number = int(input())
is_true = False
if number >= 1:
    if number in [2, 3, 5]:
        is_true = True
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        is_true = False
    else:
        is_true = True
else:
    is_true = False
print(is_true)