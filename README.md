# Student Performance Analytics System

## About the Project

The Student Performance Analytics System is a simple Python project developed to analyze student marks and attendance. It helps to calculate total marks, average marks, grades, and pass or fail results. It also provides information about class performance and identifies the top-performing students.

This project uses Python, Pandas, and NumPy to perform calculations and analyze student data.

## Objectives

* To analyze student academic performance.
* To calculate total and average marks.
* To assign grades based on student averages.
* To identify passed and failed students.
* To compare subject-wise performance.
* To find the top-performing students.
* To analyze student attendance.

## Technologies Used

* **Python:** Used to write the program and perform calculations.
* **Pandas:** Used to read and process student data.
* **NumPy:** Used for numerical calculations and result classification.
* **CSV:** Used to store student records.

## Dataset Description

The project uses a dataset containing 20 student records.

The dataset includes the following columns:

| Column     | Description               |
| ---------- | ------------------------- |
| Student_ID | Unique ID of each student |
| Name       | Student name              |
| Department | Student department        |
| Python     | Marks in Python           |
| Maths      | Marks in Mathematics      |
| Statistics | Marks in Statistics       |
| Attendance | Attendance percentage     |

## Features

1. **Total Marks:** Calculates the total marks obtained in three subjects.
2. **Average Marks:** Calculates the average marks of each student.
3. **Grade Calculation:** Assigns grades based on average marks.
4. **Pass or Fail:** Checks whether the student passes all three subjects.
5. **Class Summary:** Displays the total number of students, class average, highest average, and lowest average.
6. **Subject Analysis:** Calculates the average marks for each subject.
7. **Top 5 Students:** Displays the five students with the highest average marks.
8. **Attendance Analysis:** Calculates the average attendance of all students.

## Grade Criteria

| Average Marks | Grade |
| ------------- | ----- |
| 90 and above  | A+    |
| 80–89.99      | A     |
| 70–79.99      | B     |
| 60–69.99      | C     |
| 50–59.99      | D     |
| Below 50      | F     |

A student is considered passed when they score at least 35 marks in every subject.

## Project Structure

```text
StudentPerformanceProject/
│
├── main.py
├── students.csv
└── README.md
```

## How to Run the Project

1. Install Python on your computer.

2. Open the project folder in Visual Studio Code.

3. Install the required libraries using the command:

   ```bash
   python -m pip install pandas numpy
   ```

4. Keep `main.py` and `students.csv` in the same folder.

5. Open the terminal in VS Code.

6. Run the following command:

   ```bash
   python main.py
   ```

7. The student performance analysis will be displayed in the terminal.

## Sample Output

The program displays:

* Student details with total marks and averages.
* Grades and pass/fail results.
* Overall class performance.
* Subject-wise average marks.
* Top five students.
* Average attendance percentage.

## Learning Outcomes

Through this project, I learned how to work with CSV files, use Pandas DataFrames, perform numerical calculations using NumPy, create functions, apply conditions, and analyze student performance using Python.

## Conclusion

The Student Performance Analytics System makes student result analysis easier by performing calculations automatically. It provides a clear summary of academic performance and helps identify students who perform well and those who may need improvement.

## Author

**Name:** Tangudu Praveen Kumar
**Course:** Python with AI

## GitHub Repository

Repository Link: (https://github.com/Praveenkumar-hub431/student-performance-analytics/blob/main/README.md)
