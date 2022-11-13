number_of_lines = int(input())
list_of_positive = []
list_of_negative = []

for nums in range(number_of_lines):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive.append(current_number)
    else:
        list_of_negative.append(current_number)
print(list_of_positive)
print(list_of_negative)
print(f"Count of positives: {len(list_of_positive)}")
print(f"Sum of negatives: {sum(list_of_negative)}")
