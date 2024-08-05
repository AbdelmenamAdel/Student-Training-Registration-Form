import sqlite3
# ! ##################################### Students CRUD Operation #####################################
from models import StudentModel 
# ? #################### Create Admins Operation ####################
class StudentCRUD:
# ! #################### Database Connection and Close ####################
    def connect_db(self):
        """
        Establish a connection to the database and set up the cursor.

        Returns:
            tuple: A tuple containing the cursor and the database connection.
        """
        try:
            # ! Database Connection
            db = sqlite3.connect("Database/student_registration_system.db")
            # ! Setting Up The Cursor
            cr = db.cursor()
            print("Database connected successfully.")
            return cr, db
        except sqlite3.Error as e:
            print(f"An error occurred while connecting to the database: {e}")
            return None, None
    def close_db(self, db, cr):
        """
        Commit changes, close the cursor, and close the database connection.

        Args:
            db (sqlite3.Connection): The database connection object.
            cr (sqlite3.Cursor): The cursor object.
        """
        try:
            if cr:
                cr.close()
                print("Cursor closed successfully.")
            if db:
                db.commit()
                print("Changes committed successfully.")
                db.close()
                print("Database closed successfully.")
           
        except sqlite3.Error as e:
            print(f"An error occurred while closing the database: {e}")        
# ! ############### CRUD (Create, Read, Update, Delete) Operations ###############
    def insert_student(self, student: StudentModel):
        cr, db = self.connect_db()
        try:
            # ! Check if the student with the given email already exists
            cr.execute('SELECT COUNT(1) FROM Students WHERE email = ?', (student.email,))
            if cr.fetchone()[0] > 0:
                print(f"User with email {student.email} already exists.")
                return False  # ! Indicate that the insertion was not successful
            else:
                # ! Insert the student into the students table using a parameterized query
                cr.execute('''
                INSERT INTO Students (username, password, email, Ssh,gpa,grade,passedHours)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (student.username, student.password, student.email, student.Ssh,student.gpa,student.grade,student.passedHours))
                db.commit()
                print(f"User {student.username} added successfully.")
                return True  # ! Indicate that the insertion was successful
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the database connection
            self.close_db(db,cr)

    # ? #################### Read Admins Operation ####################
    def read_students(self,grade):
        cr, db = self.connect_db()
        try:
            # ! Read students from Table
            cr.execute("SELECT * FROM Students WHERE grade = ?", (grade,))
            students = cr.fetchall()
            print(students)
            return students  # ! Optional: Return the fetched data for further use
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the database connection
            self.close_db(db,cr)

    def search_student(self,username, password):
        # ! Connect to the SQLite database
        cr, db = self.connect_db()
        try:
            # ! Query to find the user
            cr.execute("SELECT * FROM Students WHERE username = ? AND password = ?", (username,password))
            result = cr.fetchone()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.close_db(db, cr)
            # ! Check if user is found and return result
            if result:
                print("Login successful!", result)
                return result
            else:
                print("User not found.")
                return False

    # ? #################### Update Students Operation ####################
    def update_student(self, student, id):
        cr, db = self.connect_db()
        try:
            # ! Check if the student with the given id exists
            cr.execute('SELECT COUNT(1) FROM Students WHERE uid = ?', (id,))
            if cr.fetchone()[0] > 0:
                # ! Update the student in the students table
                cr.execute('''
                UPDATE Students
                SET username = ?, password = ?, email = ?, email = ?, Ssh = ?, gpa = ?, grade = ?, passedHours = ?
                WHERE uid = ?
                ''', (student.username, student.password, student.email, student.Ssh,student.gpa,student.grade,student.passedHours,id))
                print(f"User with id {id} updated successfully.")
            else:
                print(f"User with id {id} does not exist.")
                # ! Commit the changes
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)

    # ? #################### Delete Admins Operation ####################
    def delete_student(self, Ssh):
        cr, db = self.connect_db()
        try:
            # ! Check if the student with the given id exists
            cr.execute('SELECT COUNT(1) FROM Students WHERE Ssh = ?', (Ssh,))
            if cr.fetchone()[0] > 0:
                # ! Delete the student from the students table
                cr.execute('DELETE FROM Students WHERE Ssh = ?', (Ssh,))
                print(f"User with id {Ssh} deleted successfully.")
                db.commit()  # ! Commit the changes
            else:
                print(f"User with id {Ssh} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)
    
# * ##################################### Test Admins Operations #####################################    
# student =StudentModel("seif",123,30501231556676,"seif@gmail.com",3.3,"second",66)
# user=StudentCRUD()
# user.read_students()
# user.search_student("abdo",12345)
# user.insert_student(student)
# user.read_students()