import sys
import os
import pytest

# Add project root to path so frontend modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from frontend.add_student import add_student_tab
from backend.db_helper import fetch_all_students

# ----------------------------
# Test adding a student via frontend logic
# ----------------------------
def test_frontend_add_student(monkeypatch):
    # Mock input values in Streamlit
    inputs = iter(["Test Frontend Student", "2nd Grade"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Add student
    add_student_tab()

    # Check if student exists in DB
    students = fetch_all_students()
    names = [s['name'] for s in students]
    assert "Test Frontend Student" in names
