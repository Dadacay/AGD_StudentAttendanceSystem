# data/attendance_dao.py
from config.db_connection import DBConnection

class AttendanceDAO:
    def __init__(self):
        self.conn = DBConnection().get_connection()

    def save_attendance(self, student_id, status):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO attendance (student_id, status) VALUES (?, ?)",
            (student_id, status)
        )
        self.conn.commit()

    def get_all_attendance(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        return cursor.fetchall()
