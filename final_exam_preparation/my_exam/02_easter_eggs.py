import re


def find_eggs(txt_str):
    pattern = r'[@|#]+([a-z]{3,})[@|#]+[^A-Za-z0-9]*[\/]+(\d+)[\/]+'
    matched_eggs = re.findall(pattern, txt_str)
    for matches in matched_eggs:
        color = matches[0]
        qty = int(matches[1])
        print(f"You found {qty} {color} eggs!")


text_string = input()
find_eggs(text_string)
