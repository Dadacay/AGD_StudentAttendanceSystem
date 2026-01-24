package data;

/**
 * Data Access Object (DAO)
 * Handles database operations
 */
public class AttendanceDAO {

    public void saveAttendance(String studentId, String date, String status) {
        // Simulated database operation
        System.out.println(
            "Attendance Saved -> Student ID: " + studentId +
            ", Date: " + date +
            ", Status: " + status
        );
    }

    public void getAttendanceByStudent(String studentId) {
        // Simulated fetch operation
        System.out.println(
            "Fetching attendance records for Student ID: " + studentId
        );
    }
}

