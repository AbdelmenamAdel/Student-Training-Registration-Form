import sqlite3
# ! ##################################### Admins CRUD Read Operation #####################################
from models import AdminModel 
# ? #################### Create Admins Operation ####################
class AdminCRUD:
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
    def insert_admin(self, admin: AdminModel):
        cr, db = self.connect_db()
        try:
            # ! Check if the Admin with the given email already exists
            cr.execute('SELECT COUNT(1) FROM Admins WHERE email = ?', (admin.email,))
            if cr.fetchone()[0] > 0:
                print(f"User with email {admin.email} already exists.")
                return False  # ! Indicate that the insertion was not successful
            else:
                # ! Insert the Admin into the Admins table using a parameterized query
                cr.execute('''
                INSERT INTO Admins (username, password, email, Ssh)
                VALUES (?, ?, ?, ?)
                ''', (admin.username, admin.password, admin.email, admin.Ssh))
                db.commit()
                print(f"User {admin.username} added successfully.")
                return True  # ! Indicate that the insertion was successful
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the database connection
            self.close_db(db,cr)

    # ? #################### Read Admins Operation ####################
    def read_admins(self):
        cr, db = self.connect_db()
        try:
            # ! Read Admins from Table
            cr.execute("SELECT * FROM Admins")
            admins = cr.fetchall()
            print(admins)
            return admins  # ! Optional: Return the fetched data for further use
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the database connection
            self.close_db(db,cr)

    def search_admin(self,username, password):
        # ! Connect to the SQLite database
        cr, db = self.connect_db()
        try:
           
            # ! Query to find the user
            cr.execute("SELECT * FROM Admins WHERE username = ? AND password = ?", (username,password))
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

    # ? #################### Update Admins Operation ####################
    def update_admin(self, admin, id):
        cr, db = self.connect_db()
        try:
            # ! Check if the Admin with the given id exists
            cr.execute('SELECT COUNT(1) FROM Admins WHERE uid = ?', (id,))
            if cr.fetchone()[0] > 0:
                # ! Update the Admin in the Admins table
                cr.execute('''
                UPDATE Admins
                SET username = ?, password = ?, email = ?
                WHERE uid = ?
                ''', (admin.username, admin.password, admin.email, id))
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
    def delete_admin(self, id):
        cr, db = self.connect_db()
        try:
            # ! Check if the Admin with the given id exists
            cr.execute('SELECT COUNT(1) FROM Admins WHERE uid = ?', (id,))
            if cr.fetchone()[0] > 0:
                # ! Delete the Admin from the Admins table
                cr.execute('DELETE FROM Admins WHERE uid = ?', (id,))
                print(f"User with id {id} deleted successfully.")
                db.commit()  # ! Commit the changes
            else:
                print(f"User with id {id} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return False  # ! Indicate that an error occurred
        finally:
            # ! Close the cursor and the connection
            self.close_db(db,cr)
    
# * ##################################### Test Admins Operations #####################################    
# first_user=AdminModel(username="abdo",password="1234",email="adel@gmail.com",Ssh="12345678910111")
# second_user=AdminModel(username="Mohammed Adel",password="123456",email="mo@gmail.com",Ssh="12345678910111")
# user=AdminCRUD()
# user.insert_admin(first_user)
# user.update_admin(first_user,1)
# user.read_admins()

