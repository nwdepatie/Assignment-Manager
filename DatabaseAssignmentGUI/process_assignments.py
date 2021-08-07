"""
Nick Depatie
Assignment Processes
This script houses a variety of functions used for processing data, such as analyzing list data
    and mergesorting nested lists by urgency
"""

from datetime import datetime
import math
import numpy as np
import time

class process:

    def month():
        a=listtime[0]
        if a == 'January' or a=='january' or a=='1':
            listtime[0]='1'
        if a == 'February' or a=='february' or a=='2':
            listtime[0]='2'
        if a == 'March' or a=='march' or a=='3':
            listtime[0]='3'
        if a == 'April' or a=='april' or a=='4':
            listtime[0]='4'
        if a == 'May' or a=='may' or a=='5':
            listtime[0]='5'
        if a == 'June' or a=='june' or a=='6':
            listtime[0]='6'
        if a == 'July' or a=='july' or a=='7':
            listtime[0]='7'
        if a == 'August' or a=='august' or a=='8':
            listtime[0]='8'
        if a == 'September' or a=='september' or a=='9':
            listtime[0]='9'
        if a == 'October' or a=='october' or a=='10':
            listtime[0]='10'
        if a == 'November' or a=='november' or a=='11':
            listtime[0]='11'
        if a == 'December' or a=='december' or a=='12':
            listtime[0]='12'

    def day():
        a=listtime[1]
        a=int(a)
        if a<10:
            listtime[1]=f'{a:02}'

    def time():
        endspace="."
        stringtime=listtime[2]
        stringtime=stringtime+endspace
        hour=stringtime[0:2]
        minute=stringtime[-3:-1]
        listtime[2]=hour+minute

    def timetoint(inputtime):
        global listtime, due_date  
        
        listtime=list(inputtime.split(" "))
        
        process.month()
        process.day()
        process.time()
        
        due_date=listtime[0]+listtime[1]+listtime[2]
        due_date=int(due_date)
        return due_date

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

        #print(assignmentlist)
    
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