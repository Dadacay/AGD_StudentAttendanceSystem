package service;

import data.AttendanceDAO;

/**
 * Service Layer - Business Logic
 */
public class AttendanceService {

    private AttendanceDAO attendanceDAO;

    // Constructor Injection
    public AttendanceService(AttendanceDAO attendanceDAO) {
        this.attendanceDAO = attendanceDAO;
    }

    public void markAttendance(String studentId, String date, String status) {
        // Business rules can be added here
        attendanceDAO.saveAttendance(studentId, date, status);
    }

    public void viewAttendance(String studentId) {
        attendanceDAO.getAttendanceByStudent(studentId);
    }
}

