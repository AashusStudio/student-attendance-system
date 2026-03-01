import json

FILE_NAME = "students.json"

# ---------------- LOAD DATA ---------------- #

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# ---------------- SAVE DATA ---------------- #

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Load existing data
students = load_data()

# ---------------- MAIN PROGRAM ---------------- #

while True:

    print("\n1. Add student")
    print("2. View report")
    print("3. Add Presenty")
    print("4. Exit")

    try:
        choice = int(input("Select task: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # ---------------- ADD STUDENT ---------------- #

    if choice == 1:

        student_id = input("Enter student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            continue

        if student_id in students:
            print(f"Student with ID {student_id} already exists.")
            continue

        name = input("Enter student name (Lastname Firstname Middlename): ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        try:
            roll_no = int(input("Enter student roll number: "))
        except ValueError:
            print("Roll number must be an integer.")
            continue

        students[student_id] = {
            "name": name,
            "roll_no": roll_no,
            "presenty": []
        }

        save_data(students)
        print("Student added successfully.")

    # ---------------- VIEW REPORT ---------------- #

    elif choice == 2:

        student_id = input("Enter student ID: ").strip()

        if student_id in students:
            attendance = students[student_id]["presenty"]
            name = students[student_id]["name"]

            if not attendance:
                print(f"No attendance records found for {name}.")
            else:
                print(f"Attendance record of {name}:")
                for date in attendance:
                    print("-", date)
        else:
            print(f"Student with ID {student_id} not found.")

    # ---------------- ADD PRESENTY ---------------- #

    elif choice == 3:

        student_id = input("Enter student ID: ").strip()

        if student_id in students:
            date = input("Enter date (DD-MM-YYYY): ").strip()

            if not date:
                print("Date cannot be empty.")
                continue

            if date not in students[student_id]["presenty"]:
                students[student_id]["presenty"].append(date)
                save_data(students)
                print("Attendance marked successfully.")
            else:
                print("Attendance already marked for this date.")
        else:
            print(f"Student with ID {student_id} not found.")

    # ---------------- EXIT ---------------- #

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")