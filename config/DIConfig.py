# config/DIConfig.py

from data.AttendanceDAO import AttendanceDAO
from service.AttendanceService import AttendanceService
from presentation.controllers.AttendanceController import AttendanceController
from presentation.views.AttendanceCLI import AttendanceCLI

def main():
    # Create DAO
    dao = AttendanceDAO()

    # Inject DAO → Service
    service = AttendanceService(dao)

    # Inject Service → Controller
    controller = AttendanceController(service)

    # Inject Controller → CLI View
    cli = AttendanceCLI(controller)
    cli.start()  # Launch CLI menu

if __name__ == "__main__":
    main()
