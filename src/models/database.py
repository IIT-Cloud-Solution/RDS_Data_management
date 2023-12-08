import mysql.connector

# Establish a connection to the database
def create_connection():
    
    try:
      connection = mysql.connector.connect(
          host="database-1.ctfzdglq3tet.us-east-2.rds.amazonaws.com",
          user="admin",
          password="admin1234",
          database="gitdb"
      )
    except:
      print("Exception")
    return connection