
# ! Please follow the instructures for writing a clean code 
# ! this is the start of our application 
# ! after checking the database connection

from login_view import LoginView


connection =True
if (connection):
    # Create an instance of the LoginView to run the application
    LoginView()
else:
    print ("Please check your connection with database")