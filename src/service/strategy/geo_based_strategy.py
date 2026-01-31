# service/strategy/geo_based_strategy.py
from service.strategy.attendance_strategy import AttendanceStrategy

class GeoBasedStrategy(AttendanceStrategy):
    def mark_attendance(self, student):
        return True
