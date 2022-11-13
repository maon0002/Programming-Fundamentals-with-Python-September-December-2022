def decipher(text):
    words_container = [""] * len(text)
    sentence = ""
    for word in text:
        alpha_list = ""
        digit_list = []
        numeric = ""
        alphabetic = []
        for char in word:
            if char.isdigit():
                numeric += char
            elif char.isalpha():
                alphabetic += char
        numeric = chr(int(numeric))
        alpha_list += numeric

        alphabetic[0], alphabetic[-1] = alphabetic[-1], alphabetic[0]
        alpha_list += "".join(alphabetic)

        sentence += alpha_list
        sentence += " "
    print(sentence)


message_string = input().split(" ")
decipher(message_string)
