import sqlite3


class Database:
    def __init__(self, ):
        self.db_name = "Database/student_registration_system.db"

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
       
    def save_changes(self, query, params=()):
        with sqlite3.connect(self.db_name) as con:
            cursor = con.cursor()
            cursor.execute(query, params)
            con.commit()

class CoursesRegistrationCRUD:
    # ! here we init the email to get the user id in the table not Ssh and this is not in the model
    # ! we can not save it in the model.
    # ! It inits by default with auto increment in database not manualy
    def __init__(self, email):
        self.db = Database()
        # ! علشان مبعتش الإيميل كل مره أجيب فيها ال(ايدي) للطالب
        self.email = email

    def get_subjects(self, grade):
        query = 'SELECT * FROM Courses WHERE grade = ?'
        return self.db.execute_query(query, (grade,))
    def get_student_id(self):
        query = 'SELECT sid FROM Students WHERE email = ?'
        result = self.db.execute_query(query, (self.email,))  # Tuple with one element
        if result:
            return result[0][0]
        return None 
    def get_registered_subjects(self, student_id):
        query = 'SELECT subject_name FROM Registered WHERE student_id = ?'
        res = self.db.execute_query(query, (student_id,))  # Note the tuple with one element
        subject_names = tuple([row[0] for row in res])
        if not subject_names:
            return []
        query = f'SELECT * FROM Courses WHERE name IN ({",".join("?" * len(subject_names))})'
        return self.db.execute_query(query, subject_names)

    def register_subject(self, subject_name, student_id):
        query = 'INSERT INTO Registered (subject_name, student_id) VALUES (?, ?)'
        self.db.save_changes(query, (subject_name, student_id))

    def unregister_subject(self, subject_name, student_id):
        query = 'DELETE FROM Registered WHERE subject_name = ? AND student_id = ?'
        self.db.save_changes(query, (subject_name, student_id))

