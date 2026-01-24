package config;

import data.AttendanceDAO;
import service.AttendanceService;

/**
 * Dependency Injection Configuration
 */
public class DIConfig {

    public static void main(String[] args) {

        // Create DAO
        AttendanceDAO attendanceDAO = new AttendanceDAO();

        // Inject DAO into Service
        AttendanceService attendanceService =
                new AttendanceService(attendanceDAO);

        // Simulate application flow
        attendanceService.markAttendance(
                "STU101",
                "2026-01-24",
                "Present"
        );

        attendanceService.viewAttendance("STU101");
    }
}

