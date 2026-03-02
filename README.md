# 📚 Student Attendance Management System

A simple and persistent Command Line Interface (CLI) based Student Attendance Management System built using Python and JSON for data storage.

This project demonstrates structured data handling, file persistence, input validation, and basic CRUD-style operations using pure Python.

---

## 🚀 Features

- ➕ Add new students
- 📄 View attendance report
- ✅ Mark attendance with date
- 💾 Persistent storage using JSON
- 🛡 Input validation and duplicate prevention
- 🔁 Automatic data loading on program start

---

## 🛠 Tech Stack

- Python 3.x
- JSON (for persistent storage)
- File handling

---

## 📂 Project Structure

```
student-attendance-system/
│
├── main.py
├── students.json
└── README.md
```

---

## ⚙️ How It Works

- Student data is stored in a dictionary structure.
- The dictionary is saved into a `students.json` file.
- On every program start, data is loaded automatically.
- On every update (add student / mark attendance), data is saved instantly.

Example JSON structure:

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

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student-attendance-system.git
```

2. Navigate into the project folder:

```bash
cd student-attendance-system
```

3. Run the program:

```bash
python main.py
```

---

## 📌 Learning Objectives

This project helped in understanding:

- Python dictionaries
- JSON serialization and deserialization
- File read/write modes
- Exception handling
- Input validation
- Persistent state management

---

## 👨‍💻 Author

Aashish  
Aspiring AI/ML Engineer  
Focused on building real-world Python projects step by step.

---

## 📄 License

This project is open-source and available for educational purposes.
