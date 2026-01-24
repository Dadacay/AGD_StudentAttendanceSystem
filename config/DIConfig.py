# config/DIConfig.py

from data.AttendanceDAO import AttendanceDAO
from service.AttendanceService import AttendanceService
from presentation.controllers.AttendanceController import AttendanceController

def main():
    # Create DAO
    dao = AttendanceDAO()

    # Inject DAO → Service
    service = AttendanceService(dao)

    # Inject Service → Controller
    controller = AttendanceController(service)

    # Simulate system flow
    controller.mark_attendance("STU101", "2026-01-24", "Present")
    controller.view_attendance("STU101")

if __name__ == "__main__":
    main()
