from database import create_connection

class Commit:
    def __init__(self):
        
        self.connnection = create_connection()

    def insert(self, user_id=0, date='9999-12-12', message='TESTMESSAGE', comment_count=0):
        cursor = self.connnection.cursor()
        query = "INSERT INTO Commit (user_id, date, message,comment_count) VALUES (%s, %s, %s, %s)"
        cursor.execute(query , (user_id, date[0], message, comment_count))
        self.connnection.commit()
        
      

    def insert_all(self, data_list):
      
        self.truncate()
        print("------- Table Truncated")
        for row in data_list:
            
            self.insert(row['user_id'], row['DATE'], row['Message'], str(row['comment_count']))

    def truncate(self):
        cursor = self.connnection.cursor()
        query = "TRUNCATE TABLE Commit"
        cursor.execute(query)
        self.connnection.commit()
        

    def __del__(self):
        self.connnection.close()
        print("Destructor called, Connection Closed.")
    

        


    

   
    
    


