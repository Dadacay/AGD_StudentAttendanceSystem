package test.data;

import data.AttendanceDAO;

/**
 * Test class for AttendanceDAO
 */
public class AttendanceDAOTest {

    public static void main(String[] args) {

        // Arrange
        AttendanceDAO dao = new AttendanceDAO();

        // Act
        System.out.println("Running AttendanceDAO Test...");
        dao.saveAttendance("STU301", "2026-01-24", "Absent");
        dao.getAttendanceByStudent("STU301");

        // Assert (manual verification via console output)
        System.out.println("AttendanceDAO Test Completed.");
    }
}

