from data.AttendanceDAO import AttendanceDAO

print("Running AttendanceDAO Test...")

dao = AttendanceDAO()
dao.save_attendance("STU301", "2026-01-24", "Absent")
dao.get_attendance_by_student("STU301")

print("AttendanceDAO Test Completed.")
