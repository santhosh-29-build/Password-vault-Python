from datetime import datetime

class Passkey:
    def __init__(self,user_name : str ,passkey_name : str ,password : str):
        self.__user_name=user_name
        self.__passkey_name=passkey_name
        self.__password=password
        self.created_at=datetime.today().strftime("%d-%m-%Y")

                  
    def get_passkey(self):
        return self.__passkey_name
    
    def get_user_name(self):
        return self.__user_name
    
    def get_password(self):
        return self.__password
    
    def get_date(self):
        return self.created_at
    