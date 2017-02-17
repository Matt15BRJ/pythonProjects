#Drill for Tech Academy Python Course item 62
#Get the time for two branches located in NY and London and compare
#to local time (PDX) to see if they are open
#Author: Matt Thoman

from datetime import datetime
from datetime import tzinfo
import time
from time import localtime


lt=localtime()#get the local time here in Portland
pdxTime = int(lt.tm_hour)#turn that time into an integer
#print(pdxTime)

nyTime = (pdxTime + 3)#add 3 hours to the Portland time to get NY time
#print(nyTime)

londonTime = (pdxTime + 8)#add 8 hours to get London time
#print(londonTime)


#check to see if the branches are open
def check_branch_open(pdxTime,nyTime,londonTime):
    if nyTime > 9 and nyTime < 21:
        print('The New York branch is open.')
    else:
        print('The New York branch is closed.')

    if londonTime > 9 and londonTime < 21:
        print('The London branch is open.')
    else:
        print('The London branch is closed.')


check_branch_open(pdxTime,nyTime,londonTime)    
