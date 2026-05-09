<div align="center">
# 🎓 Student Attendance Management System
 
**A lightweight, CLI-based attendance tracker built with pure Python — no external dependencies required.**
 
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
![Storage](https://img.shields.io/badge/Storage-JSON-orange?style=flat-square&logo=json&logoColor=white)
![License](https://img.shields.io/badge/License-Open%20Source-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
 
</div>
---
 
## 📖 Overview
 
A simple yet functional **Student Attendance Management System** built entirely in Python. Designed as a hands-on learning project, it demonstrates how to manage structured data, persist state across sessions using JSON, and build a clean CLI interface — all without any third-party libraries.
 
---
 
## ✨ Features
 
| Feature | Description |
|---|---|
| ➕ Add Students | Register new students with name and roll number |
| ✅ Mark Attendance | Record attendance with a specific date |
| 📄 View Reports | Display full attendance history per student |
| 💾 Persistent Storage | Data saved instantly to `students.json` |
| 🛡️ Input Validation | Prevents duplicates and invalid entries |
| 🔁 Auto Data Load | Restores previous session data on startup |
 
---
 
## 🛠️ Tech Stack
 
- **Language:** Python 3.x
- **Storage:** JSON (file-based persistence)
- **Interface:** Command Line (CLI)
- **Dependencies:** None (standard library only)
---
 
## 📂 Project Structure
 
```
student-attendance-system/
│
├── main.py            # Entry point & core logic
├── students.json      # Auto-generated persistent data store
└── README.md          # Project documentation
```
 
---
 
## ⚙️ Data Structure
 
Student records are stored as a JSON object, keyed by a unique username. Each record holds the student's name, roll number, and a list of dates they were marked present.
 
```json
{
    "aashish01": {
        "name": "Kohli Virat Prem",
        "roll_no": 1,
        "presenty": [
            "02-03-2026",
            "03-03-2026"
        ]
    }
}
```
 
---
 
## ▶️ Getting Started
 
**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/student-attendance-system.git
```
 
**2. Navigate into the project folder**
```bash
cd student-attendance-system
```
 
**3. Run the program**
```bash
python main.py
```
 
> ℹ️ No installation or setup required. The `students.json` file is created automatically on first run.
 
---
 
## 📌 What I Learned
 
This project was built to solidify core Python concepts through real-world application:
 
- **Dictionaries** — structuring and querying nested data
- **JSON serialization** — reading and writing persistent state with `json.load()` / `json.dump()`
- **File I/O** — safe file read/write with proper mode handling
- **Exception handling** — graceful error recovery for missing files or bad input
- **Input validation** — preventing duplicate entries and enforcing data integrity
- **State management** — keeping in-memory data in sync with disk storage
---
 
## 🚀 Potential Improvements
 
- [ ] Export attendance reports to CSV
- [ ] Add a search/filter feature by date or student
- [ ] Calculate attendance percentage per student
- [ ] Add a simple GUI using `tkinter`
- [ ] Migrate storage to SQLite for scalability
---
 
## 👨‍💻 Author
 
**Aashish**
Aspiring AI/ML Engineer — building real-world Python projects, one step at a time.
 
---
 
## 📄 License
 
This project is open-source and free to use for educational purposes.
 
