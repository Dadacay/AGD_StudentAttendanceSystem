# config/dao_factory.py
from data.attendance_dao import AttendanceDAO

class DAOFactory:
    @staticmethod
    def get_attendance_dao():
        return AttendanceDAO()
