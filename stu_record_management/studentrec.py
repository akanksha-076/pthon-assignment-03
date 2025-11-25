"""
NAME : AKANKSHA KUMARI
ROLL NO.:2501010076
COURSE : B.TECH CSE CORE
SECTION : A
"""

# TOPIC : STUDENT RECORD MANAGEMENT SYSTEM

students = {}  
# -----------------------------
# 1. ADDING STUDENT FUNCTION
# -----------------------------
def add_student():
    roll = int(input("Enter Roll Number: "))

    if roll in students:
        print("Student with this roll number already exists!")
        return

    name = input("Enter Student Name: ")
    math = int(input("Enter Marks obtained in MATHS: "))
    sci = int(input("Enter Marks obtained in SCIENCE: "))
    eng = int(input("Enter Marks obtained in ENGLISH: "))

    students[roll] = {
        "name": name,
        "math": math,
        "science": sci,
        "english": eng
    }

    print("Student added successfully!\n")


# -------------------------
# 2. SEARCH STUDENT
# -------------------------
def search_student():
    roll = int(input("Enter Roll Number to search: "))

    if roll not in students:
        print("No student found with this roll number.\n")
        return

    student = students[roll]
    total = student["math"] + student["science"] + student["english"]
    avg = total / 3

    print("\n--- Student Details ---")
    print(f"Name       : {student['name']}")
    print(f"Math       : {student['math']}")
    print(f"Science    : {student['science']}")
    print(f"English    : {student['english']}")
    print(f"Total Marks: {total}")
    print(f"Average    : {avg:.2f}\n")


# -------------------------
# 3. UPDATE MARKS
# -------------------------
def update_marks():
    roll = int(input("Enter Roll Number to update: "))

    if roll not in students:
        print("No student found with this roll number.\n")
        return

    print("Enter new marks:")
    math = int(input("Math: "))
    sci = int(input("Science: "))
    eng = int(input("English: "))

    students[roll]["math"] = math
    students[roll]["science"] = sci
    students[roll]["english"] = eng

    print("Marks updated successfully!\n")


# -------------------------
# 4. DELETE STUDENT
# -------------------------
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))

    if roll not in students:
        print("No student found with this roll number.\n")
        return

    del students[roll]
    print("Student record deleted successfully!\n")


# -------------------------
# 5. DISPLAY ALL STUDENTS
# -------------------------
def display_all():
    if not students:
        print("No student records found.\n")
        return

    print("\n-------------------------------------------------------------")
    print("Roll   Name            Math  Sci   Eng   Total   Average")
    print("-------------------------------------------------------------")

    for roll, details in students.items():
        total = details["math"] + details["science"] + details["english"]
        avg = total / 3

        print(f"{roll:<6} {details['name']:<15} {details['math']:<5} "
              f"{details['science']:<5} {details['english']:<5} "
              f"{total:<7} {avg:.2f}")

    print("-------------------------------------------------------------\n")


# -------------------------
# MAIN MENU LOOP
# -------------------------
def main():
    while True:
        print("=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student Marks")
        print("4. Delete Student")
        print("5. Display All Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_all()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run Program
main()