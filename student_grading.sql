-- ----------------------------------------
-- Database: student_grading
-- ----------------------------------------
CREATE DATABASE IF NOT EXISTS student_grading;
USE student_grading;

-- ----------------------------------------
-- Drop tables if they exist
-- ----------------------------------------
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

-- ----------------------------------------
-- Table: students
-- ----------------------------------------
CREATE TABLE students (
    student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    grade_level VARCHAR(50) NOT NULL
);

-- ----------------------------------------
-- Table: courses
-- ----------------------------------------
CREATE TABLE courses (
    course_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- ----------------------------------------
-- Table: grades
-- ----------------------------------------
CREATE TABLE grades (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    score INT NOT NULL,
    letter_grade VARCHAR(2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);

-- ----------------------------------------
-- Sample Data: students
-- ----------------------------------------
INSERT INTO students (name, grade_level) VALUES
('John Doe', '1st Grade'),
('Jane Smith', '2nd Grade'),
('Alice Brown', '3rd Grade'),
('Michael Johnson', '1st Grade'),
('Emily Davis', '2nd Grade');

-- ----------------------------------------
-- Sample Data: courses
-- ----------------------------------------
INSERT INTO courses (name) VALUES
('Math'),
('English'),
('Science'),
('History');

-- ----------------------------------------
-- Sample Data: grades
-- ----------------------------------------
INSERT INTO grades (student_id, course_id, score, letter_grade) VALUES
(1, 1, 95, 'A'),
(1, 2, 88, 'B'),
(2, 1, 76, 'C'),
(2, 3, 90, 'A'),
(3, 2, 85, 'B'),
(4, 1, 92, 'A'),
(5, 4, 78, 'C');
