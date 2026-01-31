# service/strategy/time_based_strategy.py
from service.strategy.attendance_strategy import AttendanceStrategy

class TimeBasedStrategy(AttendanceStrategy):
    def mark_attendance(self, student):
        return True
