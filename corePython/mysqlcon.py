from database import Database
import constants as const
mycursor = Database.getInstance()
print(mycursor)

query = "insert into users (name,username,password) values('sandeep','maurya','ramji') "
fire = mycursor.executeQuery(query)

#connection.commit()
print( "record inserted.")
print(fire)

