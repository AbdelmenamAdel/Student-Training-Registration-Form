import sqlite3

from models import CourseModel


class CoursesCRUD:
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
    def insert_course(self, course: CourseModel):
        cr, db = self.connect_db()
        try:
            # ! Check if the Course with the given name already exists
            cr.execute('SELECT COUNT(1) FROM Courses WHERE name = ?', (course.name,))
            if cr.fetchone()[0] > 0:
                print(f"Course with name {course.name} already exists.")
                return False  # ! Indicate that the insertion was not successful
            else:
                # ! Insert the Course into the Courses table using a parameterized query
                cr.execute('''
                INSERT INTO Courses (name, code, hours, grade) VALUES (?,?,?,?)''', (course.name,course.code,course.hours,course.grade))
                db.commit()  # ! Commit the changes
                print(f"Course {course.name} added successfully.")
                return True  # ! Indicate that the insertion was successful
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)
    def read_courses(self,grade):
        cr, db = self.connect_db()
        try:
            cr.execute('SELECT * FROM Courses WHERE grade = ?', (grade,))   
            courses = cr.fetchall()
            return courses  # ! Return the list of courses
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)
    def delete_course(self, cid):
        cr, db = self.connect_db()
        try:
            # ! Check if the Course with the given id exists
            cr.execute('SELECT COUNT(1) FROM Courses WHERE cid = ?', (cid,))
            if cr.fetchone()[0] > 0:
                # ! Delete the Course from the Courses table
                cr.execute('DELETE FROM Courses WHERE cid = ?', (cid,))
                db.commit()  # ! Commit the changes
                print(f"Course with id {cid} deleted successfully.")
            else:
                print(f"Course with id {cid} does not exist.")  
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)