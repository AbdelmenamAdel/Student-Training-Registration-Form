import sqlite3
# ! ##################################### Create Operation #####################################
def create_db():
    # ! Database Connection
    db = sqlite3.connect("Database/registration_form_project.db")
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
        cname VARCHAR(255) NOT NULL,
        code VARCHAR(255) NOT NULL,
        hours INTEGER NOT NULL)""")
    # ! Create Students Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Students
        (sid INTEGER PRIMARY KEY AUTOINCREMENT,
        fname VARCHAR(255) NOT NULL,
        mname VARCHAR(255) NOT NULL,
        lname VARCHAR(255) NOT NULL,
        semail VARCHAR(255) NOT NULL,
        sgpa Integer(5) NOT NULL,
        scourse VARCHAR(255) NOT NULL)""")

create_db()
