# presentation/controllers/attendance_controller.py
from service.attendance_service import AttendanceService
from service.strategy.time_based_strategy import TimeBasedStrategy

class AttendanceController:
    def __init__(self):
        self.service = AttendanceService()
        self.service.set_strategy(TimeBasedStrategy())

    def mark_button_clicked(self, student):
        self.service.mark_attendance(student)
