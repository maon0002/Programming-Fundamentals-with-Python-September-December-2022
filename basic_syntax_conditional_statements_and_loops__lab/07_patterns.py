number = int(input())

for i_up in range(number):
    print(i_up * "*")
for i_down in range(number, 0, -1):
    print(i_down * "*")
