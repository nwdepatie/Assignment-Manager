import mysql.connector
import time
from process_assignments import *
import safeguardexample as safeguard

mydb = mysql.connector.connect(
  host=process.getsublist(safeguard.host,2),
  user=process.getsublist(safeguard.user,2),
  password=process.getsublist(safeguard.password,2),
  database=process.getsublist(safeguard.database,2)
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