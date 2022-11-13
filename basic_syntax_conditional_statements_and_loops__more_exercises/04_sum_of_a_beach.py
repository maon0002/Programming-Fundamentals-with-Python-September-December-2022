import re

# text = 'WAtErSlIde'
# text = 'GolDeNSanDyWateRyBeaChSuNN'
# text = 'cItYTowNcARShoW'
text = input()
lower_text = text.lower()
search_in = ["sand", "water", "fish", "sun"]
pattern = 'sand|water|fish|sun'

counter = ""

for char in range(len(search_in)):
    current_word = search_in[char]

    if current_word in lower_text:
        counter = len(re.findall(pattern, lower_text))

if counter == "":
    print("0")
else:
    print(counter)

