# service/attendance_service.py
from config.dao_factory import DAOFactory

class AttendanceService:
    def __init__(self):
        self.dao = DAOFactory.get_attendance_dao()
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def mark_attendance(self, student):
        if self.strategy and self.strategy.mark_attendance(student):
            self.dao.save_attendance(student.id, "Present")
