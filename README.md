# AGD Student Attendance System

A **student attendance management system** is integrated, designed to simplify attendance tracking for educational institutions. This repository is a refactored version of the original project but rewritten in Python with **clean architecture and design patterns** applied to make the system modular, maintainable, and extendable.

## 🧠 Overview

The system follows a layered architecture that separates concerns between presentation, business logic, and data access. It supports role-based usage via controllers, and attendance is marked using flexible strategies.

## 🚀 Features

✔ Record student attendance  
✔ Multiple attendance strategies (e.g., time-based, geolocation-based)  
✔ Clean MVC structure  
✔ Design patterns applied:
- **Singleton** for database connection  
- **DAO** for data persistence  
- **Factory** for object creation  
- **Strategy** for attendance rules  

## 🗂️ Project Structure
AGD_StudentAttendanceSystem/
├── config/
│ ├── db_connection.py
│ └── dao_factory.py
├── data/
│ └── attendance_dao.py
├── service/
│ ├── attendance_service.py
│ └── strategy/
│ ├── attendance_strategy.py
│ ├── time_based_strategy.py
│ └── geo_based_strategy.py
├── presentation/
│ └── controllers/
│ └── attendance_controller.py
├── models/
│ └── student.py
├── main.py
└── README.md


## 🧩 Design Patterns Used

### 📌 Singleton (Database)
Ensures only a single database connection is used across the app.

### 📌 DAO (Data Access Object)
Encapsulates all database operations inside `attendance_dao.py`.

### 📌 Factory
Centralizes creation of DAO objects in `dao_factory.py`.

### 📌 Strategy
Allows pluggable attendance logic (e.g., time-based vs geolocation) using `AttendanceStrategy`.

