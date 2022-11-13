start_with = int(input())
end_with = int(input())
output = ''

for i in range(start_with, end_with + 1):
    current_char = chr(i)
    output += current_char + " "
print(output)
