class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name: str, age: int, grade: str):
        super().__init__(name, age)
        self.grade = grade

    def display_info(self) -> None:
        super().display_info()
        # print(self.name)
        # print(self.age)
        print(f"Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def display_info(self) -> None:
        super().display_info()
        print(f"Subject: {self.subject}")

    def add_student(self, student_obj: Student) -> None:
        self.students.append(student_obj)

    def list_students(self) -> None:
        print(f"Teacher {self.name} teaches:")
        for student in self.students:
            print(f" {student.name}")

if __name__ == "__main__":
    student1 = Student("Alice", 20, "A")
    student2 = Student("Bob", 22, "B")
    teacher = Teacher("Mr. Smith", 40, "Mathematics")

    people = [student1, student2, teacher]

    for person in people:
        person.display_info()

    for student in [student1, student2]:
        print(f"Teacher {teacher.name} teaches {student.name}")

    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.list_students()