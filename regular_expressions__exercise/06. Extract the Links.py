import re

pattern = r'\s?\-?(www.([a-zA-Z0-9\-\.]+)+(\.[a-z]+))'
input_line = input()

while input_line:
    output_line = re.search(pattern, input_line)

    if output_line:
        website = output_line.groups()
        print(website[0])
    input_line = input()
