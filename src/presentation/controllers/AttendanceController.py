# src/presentation/controllers/AttendanceController.py
# Controller Layer - Handles user requests and connects View to Service

class AttendanceController:
    def __init__(self, attendance_service):
        # Dependency Injection of Service
        self.attendance_service = attendance_service

    def mark_attendance(self, student_id, date, status):
        print("Controller: Processing attendance request...")
        self.attendance_service.mark_attendance(student_id, date, status)
        print("Controller: Attendance marked successfully.\n")

    def view_attendance(self, student_id):
        print("Controller: Retrieving attendance records...")
        self.attendance_service.view_attendance(student_id)
        print("Controller: Attendance displayed successfully.\n")
