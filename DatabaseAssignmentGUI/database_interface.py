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
import safeguardexample as safeguard
import time

mydb = mysql.connector.connect(
  host=process.getsublist(safeguard.host,2),
  user=process.getsublist(safeguard.user,2),
  password=process.getsublist(safeguard.password,2),
  database=process.getsublist(safeguard.database,2)
)

class send:

    def askuser():
        global name, subject, inputtime, priority, due_date, deadline
        ####################################################
        name=input("What is the name of the assignment? ")
        subject=input("What subject is this for? ")
            #due_date is in monthdaytime
        inputtime=input("When is the due date? (month day time) ")
        due_date=process.timetoint(inputtime)
        deadline=process.timeuntildeadline(due_date)
        priority=input("How important is this assignment from 1-10 (10 being the most important) ")
        
    def push_assignments(subject, name, due_date, priority):
        mycursor = mydb.cursor()
        sql = "INSERT INTO homework (subject, name, due_date, priority) VALUES (%s, %s, %s, %s)"
        
        repeat='y'

        if subject=="" or name=="" or due_date=="" or priority=="":
          print("error logging entry: entry is empty")
          return
        
        while repeat == 'y':
            
            #send.askuser()

            val = (subject, name, due_date, priority)
            
            mycursor.execute(sql, val)
            
            mydb.commit()
            
            repeat='n'
            #repeat=input('Would you like to input another assignment? (y/n) ')

        print(mycursor.rowcount, "record inserted.")

class receive:
  
  def callassignments():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM homework")

    myresult = mycursor.fetchall()

    listlength=len(myresult)

    return myresult