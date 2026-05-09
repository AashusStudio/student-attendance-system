# 📚 Student Attendance Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat-square&logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-green.svg?style=flat-square)
![License](https://img.shields.io/badge/License-Open_Source-lightgrey.svg?style=flat-square)

A lightweight, persistent Command Line Interface (CLI) application for managing student attendance. Built entirely with Python, this project demonstrates structured data handling, file persistence, input validation, and core CRUD operations without the need for external databases.

---

## 🚀 Features

*   **➕ Add New Students:** Easily register new students into the system.
*   **✅ Mark Attendance:** Record daily attendance stamped with the current date.
*   **📄 View Reports:** Generate and display a clean attendance report for all students.
*   **💾 Persistent Storage:** Data is automatically saved and retrieved using JSON, ensuring no data is lost between sessions.
*   **🛡️ Input Validation:** Built-in safeguards to prevent duplicate entries and handle invalid user inputs gracefully.
*   **🔁 Seamless Loading:** Automatically loads existing records upon program initialization.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.x
*   **Data Storage:** JSON (Standard Library)
*   **Core Concepts:** File I/O, Dictionary Manipulation, CLI Navigation

---

## 📂 Project Structure

```text
student-attendance-system/
│
├── main.py          # Main application logic and CLI loop
├── students.json    # Local database (auto-generated)
└── README.md        # Project documentation
```

---

## ⚙️ How It Works

1.  Student data is structured and stored within Python dictionaries.
2.  The dictionary state is serialized and saved into a `students.json` file.
3.  Upon startup, the script deserializes the JSON file to load existing data.
4.  Every update (adding a student or marking attendance) triggers an instant write operation to keep the local file in sync.

**Example JSON Structure (`students.json`):**
```json
{
    "aashish01": {
        "name": "Kohli Virat Prem",
        "roll_no": 1,
        "presenty": [
            "02-03-2026"
        ]
    }
}
```

---

## ▶️ How To Run

**1. Clone the repository:**
```bash
git clone https://github.com/AashusStudio/student-attendance-system.git
```

**2. Navigate into the project directory:**
```bash
cd student-attendance-system
```

**3. Execute the script:**
```bash
python main.py
```

---

## 📌 Learning Objectives

Developing this project provided hands-on experience with:
*   Python Dictionary and List manipulations
*   JSON serialization and deserialization (`json.dump`, `json.load`)
*   Secure file read/write modes and context managers (`with open(...)`)
*   Exception handling (`try-except` blocks)
*   Persistent state management in terminal applications

---

## 👨‍💻 Author

**Ashish Mangilal Choudhary**  
Aspiring Cybersecurity Professional & Software Developer  
GitHub: [@AashusStudio](https://github.com/AashusStudio)

---

## 📄 License

This project is open-source and available for educational purposes. Feel free to fork, modify, and learn from the code!
