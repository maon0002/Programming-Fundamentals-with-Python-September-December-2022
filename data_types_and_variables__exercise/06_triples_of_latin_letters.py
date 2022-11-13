letter_seq = int(input())
start_letter = 97
end_letter = letter_seq + 97

for i in range(start_letter, end_letter):
    for j in range(start_letter, end_letter):
        for k in range(start_letter, end_letter):
            letters = chr(i) + chr(j) + chr(k)
            print(letters)
