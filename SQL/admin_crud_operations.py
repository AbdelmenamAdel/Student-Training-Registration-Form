from database import cr,db
# ! CRUD (Create, Read, Update, Delete) Operations
# ! ##################################### Admins CRUD Read Operation #####################################
from Models import admins_model as model
# ? #################### Create Admins Operation ####################
def insert_admin(admin: model.AdminModel):
    # ! Insert Admin model to database
    cr.execute('SELECT COUNT(1) FROM Admins WHERE email = ?', (admin.email,))
    if cr.fetchone()[0] > 0:
        print(f"User with email {admin.email} already exists.")
    else:
        # ! Insert the Admin into the Users table using a parameterized query
        cr.execute('''
        INSERT INTO Admins (username, password, email)
        VALUES (?, ?, ?)
        ''', (admin.username, admin.password, admin.email))
        print(f"User {admin.username} added successfully.")
    # ! Commit the changes
    db.commit()
    read_admins()

# ? #################### Read Admins Operation ####################
def read_admins():
    # ! Read Admins From Table
    cr.execute("SELECT * FROM Admins")
    print(cr.fetchall())
    
# ? #################### Update Admins Operation ####################
def update_admin(admin,id):
    # ! Update Admin model in database
    cr.execute('SELECT COUNT(1) FROM Admins WHERE uid = ?', (id))
    if cr.fetchone()[0] > 0:
        # ! Update the Admin in the Users table
        cr.execute('''
        UPDATE Admins
        SET username = ?, password = ?, email = ?
        WHERE uid = ?
        ''', (admin.username, admin.password,admin.email, id))
        print(f"User with id {id} updated successfully.")
    else:
        print(f"User with id {id} does not exist.")
    # ! Commit the changes 
    db.commit()
    read_admins()
# ? #################### Delete Admins Operation ####################
def delete_admin(id):
    # ! Delete Admin model from database
    cr.execute('SELECT COUNT(1) FROM Admins WHERE uid = ?', (id))
    if cr.fetchone()[0] > 0:
        # ! Delete the Admin from the Users table
        cr.execute('DELETE FROM Admins WHERE uid = ?', (id))
        print(f"User with id {id} deleted successfully.")
    else:
        print(f"User with id {id} does not exist.")
    # ! Commit the changes 
    db.commit()
    read_admins()
    
# * ##################################### Test Admins Operations #####################################    
first_user=model.AdminModel(username="Abdelmoneim Adel",password="123456",email="abdelmenamadel96@gmail.com")
second_user=model.AdminModel(username="Mohammed Adel",password="123456",email="mo@gmail.com")
# print(first_user.username)
# insert_admin(first_user)
# insert_admin(second_user)
# delete_user('1')

