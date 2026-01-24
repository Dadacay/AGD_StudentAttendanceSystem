# AGD_StudentAttendanceSystem
# Student Attendance Management System (MVC)

## Overview
This project is a **Student Attendance Management System** developed using
the **MVC (Model–View–Controller)** pattern and **Monolithic Architecture**.

## Architecture Used
- Monolithic Architecture
- MVC Design Pattern
- Layered Architecture (Controller, Service, DAO)

## Project Structure
src/
 ├─ presentation/
 │   ├─ controllers/
 │   └─ views/
 ├─ service/
 │   └─ AttendanceService.py
 ├─ data/
 │   └─ AttendanceDAO.py
config/
 └─ DIConfig.py

## Key Features
- Mark student attendance
- View attendance records
- Clear separation of concerns
- Dependency Injection using constructor injection

## Dependency Injection
Dependencies are injected manually in `DIConfig.java` to reduce tight coupling
between layers.

## Benefits of Monolithic Architecture
- Simple to develop and deploy
- Faster internal communication
- Easier testing and debugging
- Ideal for small to medium academic systems

## How to Run
1. Compile all Java files
2. Run `DIConfig.java`
3. View output in the console

## Author
Student Attendance Management System – MVC Project
