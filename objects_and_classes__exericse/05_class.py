class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

            # print(Class.__students_count - len(self.students))

    def get_average_grade(self):
        average_grade = f"{sum(self.grades) / len(self.students):.2f}"
        average_grade = float(average_grade)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}.\nAverage grade: {self.get_average_grade():.2f}"
