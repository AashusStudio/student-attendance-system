class Present:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.present_report = []
        print("New Student Added\n")

    def student_present(self, date):
        if date not in self.present_report:
            self.present_report.append(date)
            print(f"{self.name} is registered present on [{date}]\n")

        else:
            print(f"{self.name} is already registered present on [{date}]\n")

    def view_report(self):
        if len(self.present_report) == 0:
            print(f"{self.name} has no attendance records yet.\n")
        else:
            print(f"{self.name} was present on: {self.present_report}\n")

students = {}
while True:
    print("1. Add student\n2. View Report\n3. Add Presenty\n4. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    if choice == 1:
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("Student ID already exists!\n")
            continue
        try:
            name = str(input("Enter name: "))
        except ValueError:
            print("Name must be a string.\n")
            continue
        try:
            roll_no = int(input("Enter roll no: "))
        except ValueError:
            print("Enter a valid roll number in integer\n")

        student = Present(name,roll_no)
        students[student_id] = student

    elif choice == 2:
        student_id = input("Enter the ID of student: ")
        if student_id in students:
            students[student_id].view_report()
        else:
            print("Student not found.\n")

    elif choice == 3:
        student_id = input("Enter the ID of student: ")
        if student_id in students:
            date = input("Enter the date (YYYY-MM-DD): ")
            students[student_id].student_present(date)
        else:
            print("Student not found.\n")

    elif choice == 4:
        print("Exiting program...\n")
        break

    else:
        print("Invalid choice. Try again.\n")
