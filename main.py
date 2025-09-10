from fastapi import FastAPI
from db_helper import fetch_all_students, fetch_all_courses, fetch_grade_summary

app = FastAPI()

@app.get("/students")
def get_students():
    return fetch_all_students()

@app.get("/courses")
def get_courses():
    return fetch_all_courses()

@app.get("/summary")
def get_summary():
    return fetch_grade_summary()
