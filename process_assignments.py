"""
Nick Depatie
Assignment Processes
This script houses a variety of functions used for processing data, such as analyzing list data
    and mergesorting nested lists by urgency
"""

from datetime import date, datetime
import math
from PyQt6.QtCore import QDate
import numpy as np
import time

class process:

    def timeuntildeadline(due_date):
        current_dt=datetime.now()
        current_dt= int(current_dt.strftime("%m%d%H%M"))
        deadline=due_date-current_dt
        return deadline

    def getsublist(superlist, n):
        superlist=str(superlist)

        unwantedchars="()'[]"+'"'
        for character in unwantedchars:
            superlist=superlist.replace(character,"")
        sublist=superlist.split(",")

        if n==0:
            return sublist
        elif n==1:
            return sublist[4]
        elif n==2:
            superlist=superlist.replace(",","")
            return superlist
        elif n==3:
            return sublist[1], sublist[0]
        elif n==4:
            due_date=str(sublist[2])
            due_date=due_date.strip()
            return sublist[2]
        
    def string_to_int(assignmentlist):
        
        for i in range (len(assignmentlist)):
            assignments=process.getsublist(assignmentlist[i],0)
            
            deadline=assignments[2]
            deadline=int(deadline.replace("'",""))
            deadline=process.timeuntildeadline(deadline)
            
            priority=assignments[3]
            priority=priority.replace("'","")
            priority=int(priority)
            
            urgency=deadline-(1000*priority)

            assignments.append(urgency)
            assignments=str(assignments)
            assignmentlist[i]=assignments
    
    def mergesort_list(list):
        if len(list) > 1:

            mid = len(list)//2
            left = list[:mid]
            right = list[mid:]

            process.mergesort_list(left)
            process.mergesort_list(right)

            i=0
            j=0
            k=0

            while i < len(left) and j < len(right):
                if int(process.getsublist(left[i],1)) < int(process.getsublist(right[j],1)):
                    list[k] = left[i]
                    i += 1
                    
                else:
                    list[k] = right[j]
                    j += 1
                    
                k += 1
                
            # checking that no item was left behind
            while i < len(left):
                list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                list[k] = right[j]
                j += 1
                k += 1

    def weeks_sorting(assignmentlist):
        previous_weekday=-1
        weektally=[]
        for i in range(len(assignmentlist)):
            assignment=assignmentlist[i].split(",")
            numeric_date=process.getsublist(assignment,4)
            numeric_date=(numeric_date[:-6]).strip()+" "+numeric_date[-6:-4]+" 2021"
            object_date=datetime.strptime(numeric_date,"%m %d %Y")

            current_weekday=object_date.weekday()
            #print(str(current_weekday)+"vs"+str(previous_weekday))

            #TODO IMPROVE WEEK SPECIFICTY LOGIC FOR SMALLER SAMPLE SIZES
            if current_weekday<previous_weekday:
                weektally.append(i)

            previous_weekday=current_weekday

        #print(weektally)
        for i in range(len(weektally)):
            #print(weektally[i])
            assignmentlist.insert(weektally[i]+i,"#####")
