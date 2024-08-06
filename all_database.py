import sqlite3
# ! ##################################### Create Operation #####################################
def create_db():
    # ! Database Connection
    db = sqlite3.connect("Database/student_registration_system.db")
    # ! Settings Up The Cursor
    cr = db.cursor()
    # ! CRUD (Create, Read, Update, Delete) Operations
    # ! Create Admins Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Admins
        (uid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        Ssh INTEGER NOT NULL)""")
    # ! Create Courses Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Courses
        (cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        code VARCHAR(20) NOT NULL,
        hours INTEGER NOT NULL,
        grade INTEGER NOT NULL)""")
    # ! Create Students Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Students
        (sid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        Ssh INTEGER NOT NULL,
        gpa REAL NOT NULL,
        grade VARCHAR(255) NOT NULL,       
        passedHours INTEGER NOT NULL)""")
    cr.execute("""CREATE TABLE IF NOT EXISTS Registered
        (rid INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name VARCHAR(255) NOT NULL,
        student_id INTEGER NOT NULL)""")

create_db()
