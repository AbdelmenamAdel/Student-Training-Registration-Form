
# ! Please follow the instructures for writing a clean code 
# ! this is the start of our application 
# ! after checking the database connection
connection =True
if (connection):
    from GUI.Screens import login_view as root
    obj=root.login_view("admin","1234")
else:
    print ("Please check your connection with database")