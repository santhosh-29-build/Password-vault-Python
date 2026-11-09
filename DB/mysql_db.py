import mysql.connector

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="2905",
        database="passkey_db"
    )
        
except mysql.connector.Error as e:
    print("unsucessfull")
        
    
    