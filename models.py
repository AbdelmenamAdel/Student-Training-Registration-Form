class AdminModel:
    def __init__(self, username, password, email,Ssh):
        self.username = username
        self.password = password
        self.email = email
        self.Ssh=Ssh
class StudentModel:
    def __init__(self, username,password, Ssh,email, gpa,grade, passedHours):
        self.username=username
        self.password=password
        self.email = email
        self.Ssh = Ssh
        self.gpa = gpa
        self.grade=grade
        self.passedHours = passedHours
class CourseModel:
    def __init__(self, name, code,hours,grade):
        self.name = name
        self.code = code
        self.hours=hours
        self.grade=grade