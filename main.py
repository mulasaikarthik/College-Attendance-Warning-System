def calculate_attendance(total_classes, attended_classes):
    if total_classes  <= 0:
        return 0

    percentage = (attended_classes / total_classes) * 100
    return percentage 


def attendance_status(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 65:
        return "Warning"
    else:
        return "Critical"


def exam_eligibility(percentage):
    if percentage >= 75:
        return "Eligilbe for exams"
    else:
        return "Not eligible for exams"

print("===== COLLEGE ATTENDANCE SYSTEM =====")

name = input("Enter student name: ")

total_classes = int(input("Enter Total Classes: "))
attended_classes = int(input("Enter classes attended: "))

# Validate attendance

if total_classes <= 0:
    print("\nInvalid number of total classes.")

elif attended_classes < 0:
    print("\nInvaild number of attended classes.")

elif attended_classes > total_classes:
    print("\nAttended classes cannot be greater than total classes.")

else:
    percentage = calculate_attendance(
        total_classes,
        attended_classes
    )

    status = attendance_status(percentage)
    eligibility = exam_eligibility(percentage)

    print("\n===== ATTENDANCE REPORT =====")
    print("Student Name:", name)
    print("Total Classes:", total_classes)
    print("Classes Attended:", attended_classes)
    print("Attendance:", round(percentage, 2), "%")
    print("Status:", status)
    print("Exam Status:", eligibility)

    if percentage >= 90:
        print("Excellent attendance Keep it up.")
    
    elif percentage >= 75:
        print("Your attendance is good.")

    elif percentage >= 65:
        print("Warning! Improve your attendance.")

    else:
        print("Critical attendance! You need to attend more classes.")