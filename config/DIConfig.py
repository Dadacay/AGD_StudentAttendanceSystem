# config/DIConfig.py
# Dependency Injection Configuration

from data.AttendanceDAO import AttendanceDAO
from service.AttendanceService import AttendanceService

def main():
    # Create DAO
    attendance_dao = AttendanceDAO()

    # Inject DAO into Service
    attendance_service = AttendanceService(attendance_dao)

    # Simulate application flow
    attendance_service.mark_attendance(
        "STU101",
        "2026-01-24",
        "Present"
    )

    attendance_service.view_attendance("STU101")


if __name__ == "__main__":
    main()
