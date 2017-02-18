from datetime import datetime
import time
from time import localtime
import shutil
import os


source="C:\\Users\\Owner\Desktop\\File Alpha\\"#source file path
destination="C:\\Users\\Owner\Desktop\\File Bravo\\"#destination file path
now=datetime.now()#get current time
unix=time.mktime(now.timetuple())#change current time to unix time
#print(unix)





def check_for_updated_files(unix,source,destination):
    for f in os.listdir(source):#check the files in the source dir
        if f.endswith('.txt'):
            fileTime=os.path.getmtime(source+f)#get unix time for when file was last modified
            fileName=os.path.basename(source+f)
            #print(fileTime)
    
        if (unix - fileTime) < 86400:#compare current time to when file was last modified. If modified within last 24hrs(86400 secs) move it to new loc 
            shutil.move(source+f, destination)
            print('{} changed recently, so it was moved to bravo.'.format(fileName))

        else:
            print('{} not changed recently, so it got left where it was.'.format(fileName))

check_for_updated_files(unix,source,destination)
