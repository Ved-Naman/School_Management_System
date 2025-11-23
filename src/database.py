import sqlite3
from models import Student, Teacher

DATABASE_NAME = "school_management.db"

def get_db_connection():

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            grade_level INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            teacher_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            subject TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def setup_database():

    print(f"Setting up database: {DATABASE_NAME}...")
    create_tables()
    print("Database tables created successfully.")

def add_student(student):

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (student_id, name, phone, email, grade_level) 
            VALUES (?, ?, ?, ?, ?)
        """, (student.student_id, student.name, student.phone, student.email, student.grade_level))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Student ID {student.student_id} already added earlier.")
        return False
    finally:
        conn.close()

def get_all_students():

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students ORDER BY student_id")
    rows = cursor.fetchall()
    conn.close()

    students_list = []
    for row in rows:
        student = Student(
            student_id=row['student_id'], name=row['name'], phone=row['phone'],
            email=row['email'], grade_level=row['grade_level']
        )
        students_list.append(student)
    return students_list

def get_student_by_id(student_id):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Student(
            student_id=row['student_id'], name=row['name'], phone=row['phone'],
            email=row['email'], grade_level=row['grade_level']
        )
    return None

def update_student(student_id, new_name, new_phone, new_email, new_grade):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students
        SET name = ?, phone = ?, email = ?, grade_level = ?
        WHERE student_id = ?
    """, (new_name, new_phone, new_email, new_grade, student_id))

    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    return rows_affected > 0

def delete_student(student_id):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    changed = cursor.rowcount

    conn.commit()
    conn.close()
    return rows_affected > 0
# print("Debug -> updating student", student_id)

def add_teacher(teacher):

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO teachers (teacher_id, name, phone, email, subject) 
            VALUES (?, ?, ?, ?, ?)
        """, (teacher.teacher_id, teacher.name, teacher.phone, teacher.email, teacher.subject))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Teacher ID {teacher.teacher_id} already added before.")
        return False
    finally:
        conn.close()

def get_all_teachers():

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers ORDER BY teacher_id")
    rows = cursor.fetchall()
    conn.close()

    teachers_list = []
    for row in rows:
        teacher = Teacher(
            teacher_id=row['teacher_id'], name=row['name'], phone=row['phone'],
            email=row['email'], subject=row['subject']
        )
        teachers_list.append(teacher)
    return teachers_list

def get_teacher_by_id(teacher_id):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE teacher_id = ?", (teacher_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Teacher(
            teacher_id=row['teacher_id'], name=row['name'], phone=row['phone'],
            email=row['email'], subject=row['subject']
        )
    return None

def update_teacher(teacher_id, new_name, new_phone, new_email, new_subject):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE teachers
        SET name = ?, phone = ?, email = ?, subject = ?
        WHERE teacher_id = ?
    """, (new_name, new_phone, new_email, new_subject, teacher_id))

    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    return rows_affected > 0

def delete_teacher(teacher_id):

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teachers WHERE teacher_id = ?", (teacher_id,))
    rows_affected = cursor.rowcount
    conn.commit()
    conn.close()
    return rows_affected > 0