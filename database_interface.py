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


#Imports credentials from external safeguard.py
mydb = mysql.connector.connect(
  host=process.getsublist(safeguard.host,2),
  user=process.getsublist(safeguard.user,2),
  password=process.getsublist(safeguard.password,2),
  database=process.getsublist(safeguard.database,2)
)


#Functions for interfacing with assignment database
class assignmentdatabase:

    #uploads new assignment to database with subject, name, due date, and priority
    def push_assignments(subject, name, due_date, priority):
        mycursor = mydb.cursor()
        sql = "INSERT INTO homework (subject, name, due_date, priority) VALUES (%s, %s, %s, %s)"

        #If one of the values is empty, then the assignment is not logged, as it will interfere with manipulation later
        if subject=="" or name=="" or due_date=="" or priority=="":
          print("error logging entry: entry is empty")
          return

        #executes upload
        val = (subject, name, due_date, priority)  
        mycursor.execute(sql, val)
        mydb.commit()


    #deletes a specific assignment from the database with a specific name and subject (This prevents two assignments
    # named the same thing, i.e. "Quiz 2" for two different subjects from being deleted)
    def delete_assignments(assignment,subject):
      mycursor=mydb.cursor()

      #executes deletion
      sql = "DELETE FROM homework WHERE name = %s AND subject = %s"
      val=(assignment[2:],subject)
      print(val)
      mycursor.execute(sql,val)

      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted")
      
    #fetches all assignments from database to be printed
    def callassignments():
      mycursor = mydb.cursor()

      mycursor.execute("SELECT * FROM homework")

      myresult = mycursor.fetchall()
  
      listlength=len(myresult)
      #returns list with all assignments
      return myresult

    #intializes datatable, where it drops the table, then creates a new table with a subject, name, due date, and priority
    def initialize():
      mycursor = mydb.cursor()
      #########################################################
      mycursor.execute("DROP TABLE homework")
      
      time.sleep(0.1)

      mycursor.execute("CREATE TABLE homework (subject VARCHAR(255), name VARCHAR(255), due_date VARCHAR(255), priority VARCHAR(255))")

      mycursor.execute("SHOW TABLES")

      #for x in mycursor:
      #  print(x)

      print("Finished with no errors")

class tododatabase:

    #uploads new todo to database
    def push_todo(name):
        mycursor = mydb.cursor()
        sql = "INSERT INTO todo (name) VALUES (%s)"

        #If one of the values is empty, then the assignment is not logged, as it will interfere with manipulation later
        if name=="":
          print("error logging entry: entry is empty")
          return

        #executes upload
        val = (name)  
        mycursor.execute(sql, (val,))
        mydb.commit()


    #deletes a specific todo from the database with a specific name
    def delete_todo(todo):
      mycursor=mydb.cursor()

      #executes deletion
      sql = "DELETE FROM todo WHERE name = %s"
      val=(todo)
      mycursor.execute(sql,(val,))

      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted")
      
    #fetches all todos from database to be printed
    def calltodos():
      mycursor = mydb.cursor()

      mycursor.execute("SELECT * FROM todo")

      myresult = mycursor.fetchall()
  
      listlength=len(myresult)
      #returns list with all assignments
      return myresult

    #intializes datatable, where it drops the table, then creates a new table with a name for each todo
    def initialize():
      mycursor = mydb.cursor()
      #########################################################
      try:
        mycursor.execute("DROP TABLE todo")
      except:
        print("creating new table...")
      
      time.sleep(0.1)

      mycursor.execute("CREATE TABLE todo (name VARCHAR(255))")

      mycursor.execute("SHOW TABLES")

      for x in mycursor:
        print(x)

      print("Finished with no errors")


#assignmentdatabase.initialize()
#tododatabase.initialize()
#tododatabase.push_todo("Robotics Research")
#print(tododatabase.calltodos())
#tododatabase.delete_todo("Apply to Co-ops")
