import mysql.connector
import time

mydb = mysql.connector.connect(
  host="DESKTOP-INKNB2M",
  user="nwdepatie",
  password="3mCl1de#",
  database="mydatabase"
)

class initialize:
  def initialize():
    mycursor = mydb.cursor()
    #########################################################
    mycursor.execute("DROP TABLE homework")
    
    time.sleep(0.1)

    mycursor.execute("CREATE TABLE homework (subject VARCHAR(255), name VARCHAR(255), due_date VARCHAR(255), priority VARCHAR(255))")

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
      print(x)

    print("Finished with no errors")

initialize.initialize()