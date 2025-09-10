import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.db_helper import insert_course, fetch_all_courses


def add_course_tab():
    st.header("Add New Course")

    name = st.text_input("Course Name")

    if st.button("Add Course"):
        if name:
            insert_course(name)
            st.success(f"Course '{name}' added successfully!")
        else:
            st.error("Please enter course name.")

    st.subheader("All Courses")
    courses = fetch_all_courses()
    st.table(courses)
