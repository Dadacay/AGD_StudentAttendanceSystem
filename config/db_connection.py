# config/db_connection.py
import sqlite3

class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect("attendance.db")
        return cls._instance

    def get_connection(self):
        return self.connection
