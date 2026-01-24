package test.service;

import service.AttendanceService;
import data.AttendanceDAO;

/**
 * Test class for AttendanceService
 */
public class AttendanceServiceTest {

    public static void main(String[] args) {

        // Arrange (setup dependencies)
        AttendanceDAO dao = new AttendanceDAO();
        AttendanceService service = new AttendanceService(dao);

        // Act (test service methods)
        System.out.println("Running AttendanceService Test...");
        service.markAttendance("STU201", "2026-01-24", "Present");
        service.viewAttendance("STU201");

        // Assert (manual verification via console output)
        System.out.println("AttendanceService Test Completed.");
    }
}

