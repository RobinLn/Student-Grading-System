import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from add_student import add_student_tab
from add_course import add_course_tab
from add_grade import add_grade_tab
from view_summary import view_summary_tab

st.set_page_config(page_title="Student Grading System", layout="wide")
st.title(" Student Grading System")

# Tabs
tabs = st.tabs(["Add Student", "Add Course", "Add Grade", "View Summary"])

with tabs[0]:
    add_student_tab()

with tabs[1]:
    add_course_tab()

with tabs[2]:
    add_grade_tab()

with tabs[3]:
    view_summary_tab()