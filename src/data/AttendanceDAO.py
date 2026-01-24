# data/AttendanceDAO.py
# Data Access Layer

class AttendanceDAO:
    def save_attendance(self, student_id, date, status):
        # Simulated database save
        print(
            f"Attendance Saved -> Student ID: {student_id}, "
            f"Date: {date}, Status: {status}"
        )

    def get_attendance_by_student(self, student_id):
        # Simulated database fetch
        print(f"Fetching attendance records for Student ID: {student_id}")
