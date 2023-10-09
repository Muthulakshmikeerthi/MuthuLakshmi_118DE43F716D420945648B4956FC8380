class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Sample usage
students = [
    Student("Alice", "S12345", 3.8),
    Student("Bob", "S67890", 3.5),
    Student("Charlie", "S13579", 3.9),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(student)
