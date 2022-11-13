grade_dict = {}
number_of_pairs = int(input())

for pairs in range(number_of_pairs):
    student, grade, = input(), float(input())
    if student not in grade_dict.keys():
        grade_dict[student] = []
    grade_dict[student].append(grade)

for name, grades in grade_dict.items():
    averageGrade = sum(grades) / len(grades)
    if averageGrade >= 4.50:
        print(f"{name} -> {averageGrade:.2f}")
