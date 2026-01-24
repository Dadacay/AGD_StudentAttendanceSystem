# src/presentation/views/AttendanceCLI.py
# Simple CLI-based View

from presentation.controllers.AttendanceController import AttendanceController

class AttendanceCLI:
    def __init__(self, controller: AttendanceController):
        self.controller = controller

    def start(self):
        while True:
            print("\n=== Student Attendance Management System ===")
            print("1. Mark Attendance")
            print("2. View Attendance")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                student_id = input("Enter Student ID: ")
                date = input("Enter Date (YYYY-MM-DD): ")
                status = input("Enter Status (Present/Absent): ")
                self.controller.mark_attendance(student_id, date, status)

            elif choice == "2":
                student_id = input("Enter Student ID: ")
                self.controller.view_attendance(student_id)

            elif choice == "3":
                print("Exiting Student Attendance System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
