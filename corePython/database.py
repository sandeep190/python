import constants
import mysql.connector

class Database:
    __instance = None
    @staticmethod 
    def getInstance():
        if Database.__instance == None :
            mydb = mysql.connector.connect(user=constants.MY_USER ,
                                                          password='',
                                                          host=constants.MY_HOST,
                                                          database=constants.MY_DB)
            Database.__instance = mydb.cursor()
        return Database.__instance
    
    def executeQuery(self,query):
        print("come here")
        print(self.__instance)
        return self.__instance.execute(query)
        
    
    def __init__(self):
        if Database.__instance != None :
            raise Exception ("This is not singloton class")
        else :
            Database.__instance = self
            
   
            