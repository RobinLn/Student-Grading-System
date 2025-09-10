import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.db_helper import insert_student, fetch_all_students


def add_student_tab():
    st.header("Add New Student")

    name = st.text_input("Student Name")
    grade_level = st.selectbox("Grade Level",
                               ["Kindergarten", "1st Grade", "2nd Grade", "3rd Grade", "4th Grade", "5th Grade"])

    if st.button("Add Student"):
        if name:
            insert_student(name, grade_level)
            st.success(f"Student '{name}' added successfully!")
        else:
            st.error("Please enter student name.")

    st.subheader("All Students")
    students = fetch_all_students()
    st.table(students)
