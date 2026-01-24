from service.AttendanceService import AttendanceService
from data.AttendanceDAO import AttendanceDAO

print("Running AttendanceService Test...")

dao = AttendanceDAO()
service = AttendanceService(dao)

service.mark_attendance("STU201", "2026-01-24", "Present")
service.view_attendance("STU201")

print("AttendanceService Test Completed.")
