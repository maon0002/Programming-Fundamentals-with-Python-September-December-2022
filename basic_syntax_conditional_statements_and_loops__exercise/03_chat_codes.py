codes_qty = int(input())

for i in range(codes_qty):
    input_line = int(input())
    if input_line == 88:
        print("Hello")
    elif input_line == 86:
        print("How are you?")
    elif not input_line == 88 and not input_line == 86 and input_line < 88:
        print("GREAT!")
    elif input_line > 88:
        print("Bye.")
