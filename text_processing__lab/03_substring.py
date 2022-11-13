first_string = input()
second_string = input()
output_string = second_string
while first_string in output_string:
    output_string = output_string.replace(first_string, "")
print(output_string)
