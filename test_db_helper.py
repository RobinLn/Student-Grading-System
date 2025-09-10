import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from backend.db_helper import insert_student, fetch_all_students, insert_course, fetch_all_courses, insert_grade, fetch_grade_summary


def test_add_student():
    insert_student("Test Student", "1st Grade")
    students = fetch_all_students()
    names = [s['name'] for s in students]
    assert "Test Student" in names


def test_add_course():
    insert_course("Test Course")
    courses = fetch_all_courses()
    names = [c['name'] for c in courses]
    assert "Test Course" in names


def test_add_grade():
    students = fetch_all_students()
    courses = fetch_all_courses()
    student_id = students[0]['student_id']
    course_id = courses[0]['course_id']

    insert_grade(student_id, course_id, 95, "A")
    summary = fetch_grade_summary()
    found = False
    for record in summary:
        if record['student_id'] == student_id and record['course_id'] == course_id and record['letter_grade'] == "A":
            found = True
            break
    assert found
