# service/strategy/attendance_strategy.py
from abc import ABC, abstractmethod

class AttendanceStrategy(ABC):

    @abstractmethod
    def mark_attendance(self, student):
        pass
