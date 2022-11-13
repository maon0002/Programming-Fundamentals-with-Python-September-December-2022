def emoticons(text):
    for i in range(len(text)):
        char = text[i]
        if char == ":":
            next_char = text[i + 1]
            print(f"{char}{next_char}")
        else:
            pass


input_string = input()
emoticons(input_string)
