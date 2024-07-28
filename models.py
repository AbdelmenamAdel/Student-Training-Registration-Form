class AdminModel:
    def __init__(self, username, password, email,Ssh):
        self.username = username
        self.password = password
        self.email = email
        self.Ssh=Ssh
class StudentModel:
    def __init__(self, fname, mname, lname, semail, sgpa, scourse):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.semail = semail
        self.sgpa = sgpa
        self.scourse = scourse
class CourseModel:
    def __init__(self, cname, cdescription):
        self.cname = cname
        self.code = cdescription