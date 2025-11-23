from models import Student, Teacher
from database import (
    setup_database, add_student, get_all_students, get_student_by_id,
    update_student, delete_student, add_teacher, get_all_teachers,
    get_teacher_by_id, update_teacher, delete_teacher
)
import sys

def display_menu():

    print("School Management System (CLI)")
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Exit")

def student_menu():

    print("\n Student Management ")
    print("1. Add New Student (C)")
    print("2. View All Students (R)")
    print("3. Update Student Details (U)")
    print("4. Delete Student (D)")
    print("5. Back to Main Menu")
    return input("Enter choice: ")

def teacher_menu():

    print("\n Teacher Management ")
    print("1. Add New Teacher (C)")
    print("2. View All Teachers (R)")
    print("3. Update Teacher Details (U)")
    print("4. Delete Teacher (D)")
    print("5. Back to Main Menu")
    return input("Enter choice: ")

def display_students(students):

    if not students:
        print("\nNo students found in the database. ")
        return



    print("CURRENT STUDENT ROSTER")
    print("ID | Name | Grade | Email")


    for student in students:
        row_data = f"{student.student_id:<8} {student.name:<25} {str(student.grade_level):<8} {student.email:<25}"
        print(row_data)

def display_teachers(teachers):

    if not teachers:
        print("\nNo teachers found in the database. ")
        return

    print("CURRENT TEACHER ROSTER")
    print("ID | Name | Grade | Email")


    for teacher in teachers:
        row_data = f"{teacher.teacher_id:<8} {teacher.name:<25} {teacher.subject:<15} {teacher.email:<25}"
        print(row_data)

def get_student_data():

    print("\nEnter new student details:")
    student_id = input("Student ID (e.g., S101): ").strip()
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    try:
        grade_level = int(input("Grade Level (e.g., 10): ").strip())

    except ValueError:

        print("Invalid Grade Level. Please re-enter.")
        return None

    return Student(student_id, name, phone, email, grade_level)
tmp = get_all_students()


def get_teacher_data():

    print("\nEnter new teacher details:")
    teacher_id = input("Teacher ID (e.g., T501): ").strip()
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    subject = input("Subject Taught: ").strip()
    return Teacher(teacher_id, name, phone, email, subject)

def handle_update_student():

    student_id = input("Enter Student ID to update (e.g., S101): ").strip()
    student = get_student_by_id(student_id)
    if not student:
        print(f"Error: Student with ID {student_id} not found.")

        return

    print("\nCurrent Details")
    print(f"ID: {student.student_id}, Name: {student.name}, Grade: {student.grade_level}")
    print("\nEnter new values (Leave field blank to keep current value):")

    new_name = input(f"New Name ({student.name}): ") or student.name
    new_phone = input(f"New Phone ({student.phone}): ") or student.phone
    new_email = input(f"New Email ({student.email}): ") or student.email

    current_grade = str(student.grade_level)
    new_grade_input = input(f"New Grade Level ({current_grade}): ")

    new_grade = int(new_grade_input.strip()) if new_grade_input else student.grade_level

    if update_student(student.student_id, new_name, new_phone, new_email, new_grade):
        print(f"\nStudent ID {student.student_id} updated successfully!")

    else:
        print(f"Failed to update student ID {student.student_id}.")

def handle_delete_student():

    student_id = input("Enter Student ID to delete (e.g., S101): ").strip()
    student = get_student_by_id(student_id)
    if not student:
        print(f"Error: Student with ID {student_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete student {student.name} (ID: {student_id})? (yes/no): ").lower()

    if confirm == 'yes':
        if delete_student(student_id):
            print(f"\nStudent ID {student_id} deleted successfully.")

        else:
            print(f"Failed to delete student ID {student_id}.")

    else:
        print("Delete operation canceled.")

def handle_update_teacher():

    teacher_id = input("Enter Teacher ID to update (e.g., T501): ").strip()
    teacher = get_teacher_by_id(teacher_id)

    if not teacher:
        print(f"Error: Teacher with ID {teacher_id} not found.")
        return

    print("\nCurrent Details")
    print(f"ID: {teacher.teacher_id}, Name: {teacher.name}, Subject: {teacher.subject}")

    print("\nEnter new values (Leave field blank to keep current value):")



    new_name = input(f"New Name ({teacher.name}): ") or teacher.name
    new_phone = input(f"New Phone ({teacher.phone}): ") or teacher.phone
    new_email = input(f"New Email ({teacher.email}): ") or teacher.email
    new_subject = input(f"New Subject Taught ({teacher.subject}): ") or teacher.subject

    if update_teacher(teacher.teacher_id, new_name, new_phone, new_email, new_subject):
        print(f"\nTeacher ID {teacher.teacher_id} updated successfully!")
    else:
        print(f"Failed to update teacher ID {teacher.teacher_id}.")


def handle_delete_teacher():

    teacher_id = input("Enter Teacher ID to delete (e.g., T501): ").strip()
    teacher = get_teacher_by_id(teacher_id)
    if not teacher:
        print(f"Error: Teacher with ID {teacher_id} not found.")

        return

    confirm = input(f"Are you sure you want to delete teacher {teacher.name} (ID: {teacher_id})? (yes/no): ").lower()

    if confirm == 'yes':
        if delete_teacher(teacher_id):
            print(f"\nTeacher ID {teacher_id} deleted successfully.")
        else:
            print(f"Failed to delete teacher ID {teacher_id}.")
    else:
        print("Delete operation canceled.")

def handle_student_management():

    while True:
        choice = student_menu()
        if choice == '1':
            student_obj = get_student_data()
            if student_obj:
                if add_student(student_obj):
                    print(f"\nStudent '{student_obj.name}' added successfully.")
        elif choice == '2':
            students_list = get_all_students()
            display_students(students_list)

        elif choice == '3':
            handle_update_student()
        elif choice == '4':

            handle_delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

def handle_teacher_management():

    while True:
        choice = teacher_menu()
        if choice == '1':
            teacher_obj = get_teacher_data()
            if teacher_obj:
                if add_teacher(teacher_obj):
                    print(f"\nTeacher '{teacher_obj.name}' added successfully.")
        elif choice == '2':
            teachers_list = get_all_teachers()
            display_teachers(teachers_list)
        elif choice == '3':
            handle_update_teacher()
        elif choice == '4':
            handle_delete_teacher()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():

    setup_database()

    while True:
        display_menu()
        main_choice = input("Your choice: ")

        if main_choice == '1':
            handle_student_management()
        elif main_choice == '2':
            handle_teacher_management()

        elif main_choice == '3':
            print("\n👋 Exiting School Management System. Goodbye!")
            sys.exit(0)

        else:
            print("wrong option, try again")


if __name__ == '__main__':
    main()