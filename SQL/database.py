import sqlite3
# ! Database Connection
db = sqlite3.connect("SQL/Database/app.db")
# ! Settings Up The Cursor
cr = db.cursor()
# ! CRUD (Create, Read, Update, Delete) Operations
# ! ##################################### Create Operation #####################################
def create_db():
    # ! Create Admins Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Admins
        (uid INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL)""")
    # cr.commit()
    # ! Create Courses Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Courses
        (cid INTEGER PRIMARY KEY AUTOINCREMENT,
        cname VARCHAR(255) NOT NULL,
        cdescription VARCHAR(255) NOT NULL)""")
    # cr.commit()
    # ! Create Students Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Students
        (sid INTEGER PRIMARY KEY AUTOINCREMENT,
        fname VARCHAR(255) NOT NULL,
        mname VARCHAR(255) NOT NULL,
        lname VARCHAR(255) NOT NULL,
        semail VARCHAR(255) NOT NULL,
        sgpa Integer(5) NOT NULL,
        scourse VARCHAR(255) NOT NULL)""")
    # cr.commit()
    # ! Create Teachers Table
    cr.execute("""CREATE TABLE IF NOT EXISTS Doctors
        (tid INTEGER PRIMARY KEY AUTOINCREMENT,
        tname VARCHAR(255) NOT NULL,
        temail VARCHAR(255) NOT NULL,
        tcourse VARCHAR(255) NOT NULL)""")
    # cr.commit()
create_db()
print("Database Created Successfully")