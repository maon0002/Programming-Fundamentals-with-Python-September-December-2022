class Party:

    def __init__(self):
        self.people = []


party = Party()
while True:

    command = input()
    if command == "End":
        break
    name = command
    party.people.append(name)

first_output = f"Going: {', '.join(party.people)}"
second_output = f"Total: {len(party.people)}"
result = f"{first_output}\n{second_output}"
print(result)
