input_string = input().split()
output_string = ''
for string in input_string:
    output_string += string * (len(string))

print(output_string)
