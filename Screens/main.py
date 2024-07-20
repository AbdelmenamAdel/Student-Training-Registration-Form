
# ! Please follow the instructures for writing a clean code 
# ! this is the start of our application 
# ! after checking the database connection
connection =True
if (connection):
    import login_view as root
else:
    print ("Please check your connection with database")