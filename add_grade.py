import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.db_helper import insert_grade, fetch_all_students, fetch_all_courses


def add_grade_tab():
    st.header("Add Grade")

    students = fetch_all_students()
    courses = fetch_all_courses()

    student_dict = {s['name']: s['student_id'] for s in students}
    course_dict = {c['name']: c['course_id'] for c in courses}

    student_name = st.selectbox("Select Student", list(student_dict.keys()))
    course_name = st.selectbox("Select Course", list(course_dict.keys()))
    score = st.number_input("Score", min_value=0, max_value=100)

    if st.button("Add Grade"):
        letter_grade = get_letter_grade(score)
        insert_grade(student_dict[student_name], course_dict[course_name], score, letter_grade)
        st.success(f"Grade added: {student_name} - {course_name} - {score} ({letter_grade})")


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
