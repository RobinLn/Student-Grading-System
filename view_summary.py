import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.db_helper import fetch_grade_summary


def view_summary_tab():
    st.header("Grade Summary per Course")

    summary = fetch_grade_summary()

    st.table(summary)
