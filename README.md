# Student Grading System

This project is a student grading system that consists of a Streamlit frontend application and a MySQL backend database.

---

## Project Structure

- **frontend/**: Contains the Streamlit application code.  
- **backend/**: Contains the MySQL database helper functions.  
- **tests/**: Contains the test cases for backend and frontend.  
- **student_grading_full.sql**: SQL script to create the database and sample data.  
- **README.md**: Provides an overview and instructions for the project.  



## Setup Instructions

1. **Clone the repository**:
   
   git clone https://github.com/yourusername/student-grading-system.git
   cd student-grading-system

   Install dependencies:
pip install -r backend/requirements.txt
Create the MySQL database:

source student_grading_full.sql;

Run the Streamlit app:
streamlit run frontend/app.py

Run tests (optional):
pytest

## Screenshots

### Home Page
![Home Page](screenshots/app_home.png)

### Add Grade
![Add Grade](screenshots/add_grade.png)
