class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        # print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


messages = []
while True:

    command = input()
    if command == "Stop":
        break

    sender, receiver, content = command.split(' ')
    message = Email(sender, receiver, content)
    messages.append(message)

indices = list(map(int, input().split(', ')))
for position in indices:
    messages[position].send()

for email in messages:
    print(email.get_info())
