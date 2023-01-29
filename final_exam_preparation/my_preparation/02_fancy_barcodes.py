import re


def barcode_validation(barcode_str):
    pattern = r'([@][#]+[A-Z]{1}[A-Za-z0-9]{4,}[A-Z][@][#]+)'
    if not re.match(pattern, barcode_str):
        print("Invalid barcode")
        return "Invalid barcode"

    pattern_digits = r'(\d)'
    if re.findall(pattern_digits, barcode_str):
        match_digits = re.findall(pattern_digits, barcode_str)
        match_digits = "".join([x for x in match_digits])
        print(f"Product group: {match_digits}")
        return f"Product group: {match_digits}"
    else:
        print("Product group: 00")
        return "Product group: 00"


def barcodes(num):
    for _ in range(num):
        current_barcode = input()
        barcode_validation(current_barcode)
    return None


num_of_inputs = int(input())
barcodes(num_of_inputs)
