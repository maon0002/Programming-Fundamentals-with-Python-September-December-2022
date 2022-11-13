# first_string = "Kitty"
# second_string = "Doggy"
first_string = input()
second_string = input()
mutation = ""
antimutation = ""

for i in range(1, len(first_string) + 1):
    mutation += second_string[:i] + first_string[i:]

    if mutation != first_string and mutation != antimutation:
        print(mutation)
        antimutation = mutation
        mutation = ""
    else:
        mutation = ""
        continue
