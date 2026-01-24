# service/AttendanceService.py
# Business Logic Layer

class AttendanceService:
    def __init__(self, attendance_dao):
        # Dependency Injection
        self.attendance_dao = attendance_dao

    def mark_attendance(self, student_id, date, status):
        # Business rules can be added here
        self.attendance_dao.save_attendance(student_id, date, status)

    def view_attendance(self, student_id):
        self.attendance_dao.get_attendance_by_student(student_id)
