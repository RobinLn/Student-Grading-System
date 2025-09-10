import mysql.connector
from contextlib import contextmanager

# -------------------- DATABASE CONFIG --------------------
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "database": "student_grading"
}

@contextmanager
def get_db_cursor(commit=False):
    """Context manager for MySQL cursor with optional commit"""
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

# -------------------- STUDENTS --------------------
def fetch_all_students():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

def insert_student(name, grade_level):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO students (name, grade_level) VALUES (%s, %s)",
            (name, grade_level)
        )

def delete_student(student_id):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )

# -------------------- COURSES --------------------
def fetch_all_courses():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM courses")
        return cursor.fetchall()

def insert_course(course_name):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO courses (name) VALUES (%s)",
            (course_name,)
        )

def delete_course(course_id):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM courses WHERE course_id = %s",
            (course_id,)
        )

# -------------------- GRADES --------------------
def fetch_grades_by_student(student_id):
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT s.name AS student_name, s.grade_level, c.name AS course_name, g.score, g.letter_grade
               FROM grades g
               JOIN students s ON g.student_id = s.student_id
               JOIN courses c ON g.course_id = c.course_id
               WHERE g.student_id = %s''',
            (student_id,)
        )
        return cursor.fetchall()

def insert_grade(student_id, course_id, score, letter_grade):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO grades (student_id, course_id, score, letter_grade) VALUES (%s, %s, %s, %s)",
            (student_id, course_id, score, letter_grade)
        )

def delete_grade(grade_id):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "DELETE FROM grades WHERE id = %s",
            (grade_id,)
        )

# -------------------- SUMMARY --------------------
def fetch_grade_summary():
    with get_db_cursor() as cursor:
        cursor.execute('''
            SELECT g.id, g.student_id, g.course_id, g.score, g.letter_grade,
                   s.name AS student_name, c.name AS course_name
            FROM grades g
            JOIN students s ON g.student_id = s.student_id
            JOIN courses c ON g.course_id = c.course_id;
        ''')
        data = cursor.fetchall()
        return data
