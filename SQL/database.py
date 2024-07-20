
# ! Database Creation
import sqlite3
# ! Database Connection
db = sqlite3.connect("SQL/Database/app.db")
# ! Database Cursor
cursor = db.cursor()
# ! CRUD Operations
# ! Create Users Table 
db.execute("""CREATE TABLE IF NOT EXISTS Users
    (uid INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL)""")
db.commit()
# ! Create Courses Table
db.execute("""CREATE TABLE IF NOT EXISTS Courses
    (cid INTEGER PRIMARY KEY AUTOINCREMENT,
    cname VARCHAR(255) NOT NULL,
    cdescription VARCHAR(255) NOT NULL)""")
db.commit()
# ! Create Students Table
db.execute("""CREATE TABLE IF NOT EXISTS Students
    (sid INTEGER PRIMARY KEY AUTOINCREMENT,
    fname VARCHAR(255) NOT NULL,
    mname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    semail VARCHAR(255) NOT NULL,
    sgpa Integer(5) NOT NULL,
    scourse VARCHAR(255) NOT NULL)""")
db.commit()
# ! Create Teachers Table
db.execute("""CREATE TABLE IF NOT EXISTS Teachers
    (tid INTEGER PRIMARY KEY AUTOINCREMENT,
    tname VARCHAR(255) NOT NULL,
    temail VARCHAR(255) NOT NULL,
    tcourse VARCHAR(255) NOT NULL)""")
db.commit()