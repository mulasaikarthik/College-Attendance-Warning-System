# 🎓 College Attendance Warning System

A beginner-friendly **College Attendance Warning System built with Python**.

This program takes a student's total classes and attended classes, calculates the attendance percentage, determines the attendance status, and checks whether the student is eligible for exams.

## 🚀 Features

* 👨‍🎓 Takes student name as input
* 📚 Takes total classes and attended classes
* 📊 Calculates attendance percentage
* ⚠️ Identifies attendance status
* 🎓 Checks exam eligibility
* ❌ Handles invalid attendance inputs
* 🧩 Uses multiple Python functions
* 🖥️ Simple command-line interface

## 📋 Attendance Categories

| Attendance   | Status    |
| ------------ | --------- |
| 90% or above | Excellent |
| 75% – 89.99% | Good      |
| 65% – 74.99% | Warning   |
| Below 65%    | Critical  |

### Exam Eligibility

* **75% or above** → Eligible for exams
* **Below 75%** → Not eligible for exams

> Note: The eligibility rules in this project are simplified for programming practice. Actual college attendance rules may differ.

## 🛠️ Python Concepts Used

This project helped me practice:

* `input()`
* `int()`
* `def`
* Functions
* Function parameters
* `return`
* `if`
* `elif`
* `else`
* Arithmetic calculations
* Variables
* Input validation
* `round()`

## 🧮 Attendance Formula

```text
Attendance Percentage =
(Classes Attended / Total Classes) × 100
```

### Example

```text
Total Classes = 100
Classes Attended = 82

Attendance = (82 / 100) × 100
Attendance = 82%
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd college-attendance-system
```

### 3. Run the Python program

```bash
python attendance_system.py
```

## 💻 Example Output

```text
===== COLLEGE ATTENDANCE SYSTEM =====

Enter student name: Karthik
Enter total classes: 100
Enter classes attended: 82

===== ATTENDANCE REPORT =====
Student Name: Karthik
Total Classes: 100
Classes Attended: 82
Attendance: 82.0 %
Status: Good
Exam Status: Eligible for exams
Your attendance is good.
```

## ❌ Input Validation

The program checks for invalid situations such as:

```text
Total classes <= 0
Attended classes < 0
Attended classes > Total classes
```

For example:

```text
Enter total classes: 50
Enter classes attended: 60

Attended classes cannot be greater than total classes.
```

## 🔮 Future Improvements

Possible improvements for future versions:

* Calculate classes required to reach 75%
* Support multiple students
* Store attendance records
* Add a menu system
* Use lists and dictionaries
* Save data to a file
* Add a graphical user interface
* Create a web-based attendance system
* Connect the system to a database

## 📚 Learning Goal

This project is part of my **Python learning journey** and was created to practice turning basic programming concepts into a small real-world application.

The project focuses on breaking a problem into smaller functions instead of putting all the logic into one block of code.

## 👨‍💻 Author

**Sai Karthik**

BTech CSE – Data Science Student

---

⭐ If you found this project useful, feel free to star the repository!
