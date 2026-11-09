from passkey_manager.passkey import Passkey
from DB.mysql_db import mydb

class Crud:
    cursor=mydb.cursor()
    def create_passkey(self,key : Passkey):
        try:
            query="INSERT INTO passkey_tbl(user_name,passkey_name,password,created_at) VALUES(%s,%s,%s,%s)"
            values=(key.get_user_name(),key.get_passkey(),key.get_password(),key.get_date())
            self.cursor.execute(query,values)
            mydb.commit()
            
            print("sucess")
            mydb.close()
        except Exception as e:
            mydb.rollback()
            print("Mysql Error :",e)
            
    def update_passkey(self,id : int,choice : int):
        try:
            match choice:
                case 1:
                    user_name=input("Enter the New Label Name : ")
                    query="update passkey_tbl set user_name=%s where id=%s"
                    values=(user_name,id)
                    self.cursor.execute(query,values)
                    mydb.commit()
                    print("Updated Successfully") 
                    
                case 2:
                    passkey_name=input("Enter the New Passkey Name : ")
                    query="update passkey_tbl set passkey_name=%s where id=%s"
                    values=(passkey_name,id)
                    self.cursor.execute(query,values)
                    mydb.commit()
                    print("Updated Successfully") 
                                    
                case 3:
                    password=input("Enter the New Password : ")
                    query="update passkey_tbl set password=%s where id=%s"
                    values=(password,id)
                    self.cursor.execute(query,values)
                    mydb.commit()
                    print("Updated Successfully") 
                                    
                case _:
                    print("Invalid Options")
            
            mydb.close()
        except Exception as e:
            mydb.rollback()
            print("Mysql error : ",e)
        
    def delete_passkey(self,id):
        try:
            query="delete from passkey_tbl where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            mydb.commit()
            print("sucess")
        except Exception as e:
            mydb.rollback()
            print("Mysql Error :",e)
            
    def display_passkey(self):
        try:
            self.cursor.execute("select * from passkey_tbl")
            records = self.cursor.fetchall()
            
            for row in records:
                print(row)
                
            self.cursor.close()
            mydb.close()
        except Exception as e:
            print("Mysql Error :",e)
            
crud=Crud()
crud.display_passkey()
        
        



        