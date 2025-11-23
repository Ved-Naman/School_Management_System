class Person:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class Student(Person):

    def __init__(self, student_id, name, phone, email, grade_level):
        super().__init__(name, phone, email)
        self.student_id = student_id
        self.grade_level = grade_level

    def __str__(self):
        return f"Student({self.student_id}, {self.name}, grade={self.grade_level})"


class Teacher(Person):

    def __init__(self, teacher_id, name, phone, email, subject):
        super().__init__(name, phone, email)
        self.teacher_id = teacher_id
        self.subject = subject

    def __str__(self):
        return f"TEACHER | ID: {self.teacher_id} | Name: {self.name} | Subject: {self.subject}"
    def get_contact(self):
        return f"{self.name} - {self.email}"
