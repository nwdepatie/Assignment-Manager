"""
Nick Depatie
Database Interface
This script interfaces with the database to retrieve and send data for use in processing
  and GUI display.

This script uses database credentials to access the database:
  -These credentials are listed in a seperate script to maintain privacy
  -An example script has been provided to fill in with personal database info
"""


from re import A
import mysql.connector
from process_assignments import *
import safeguard as safeguard
import time

mydb = mysql.connector.connect(
  host=process.getsublist(safeguard.host,2),
  user=process.getsublist(safeguard.user,2),
  password=process.getsublist(safeguard.password,2),
  database=process.getsublist(safeguard.database,2)
)

class send:
    def push_assignments(subject, name, due_date, priority):
        mycursor = mydb.cursor()
        sql = "INSERT INTO homework (subject, name, due_date, priority) VALUES (%s, %s, %s, %s)"

        if subject=="" or name=="" or due_date=="" or priority=="":
          print("error logging entry: entry is empty")
          return

        val = (subject, name, due_date, priority)  
        mycursor.execute(sql, val)
        mydb.commit()

    def delete_assignments(assignment,subject):
      mycursor=mydb.cursor()

      sql = "DELETE FROM homework WHERE name = %s AND subject = %s"
      val=(assignment[2:],subject)
      print(val)
      mycursor.execute(sql,val)

      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted")
      


class receive:
  def callassignments():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM homework")

    myresult = mycursor.fetchall()

    listlength=len(myresult)

    return myresult

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