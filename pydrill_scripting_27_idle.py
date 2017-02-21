from datetime import datetime
import time
from time import localtime
import shutil
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pydrill_gui_34_idle
import pydrill_table_34_idle

#source="C:\\Users\\Owner\Desktop\\File Alpha\\"#source file path
#destination="C:\\Users\\Owner\Desktop\\File Bravo\\"#destination file path

#print(unix)





def check_for_updated_files(self):
    now=datetime.now()#get current time to create the time of this check
    print(now)
    conn=sqlite3.connect('filemover.db')
    with conn:
        cur=conn.cursor()
        cur.execute("""SELECT max(col_fileCheck) FROM tbl_filemover""")
        lastCheck=cur.fetchone()[0]
    conn.close()
    print(lastCheck)
    unix=time.mktime(now.timetuple())#change this checks time to unix time to be stored as the new lastCheck
    source=self.txt_choose.get()
    destination=self.txt_dest.get()
    print('source{}'.format(source))
    print('destination {}'.format(destination))
    if (source != destination) and (len(source)>0) and (len(destination)>0):#check to make sure source and destination are different and that something was chosen
        response=messagebox.askokcancel("Proceed with Changes","Updated files from {} \nwill be transferred to {}. \nDo you wish to proceed?".format(source,destination))
        if response:
            for f in os.listdir(source):#check the files in the source dir
                if f.endswith('.txt'):#checks for txt files can be taken out to check for other files
                    fileTime=os.path.getmtime(source+'/'+f)#get unix time for when file was last modified
                    fileName=(source+'/'+f)
                    #print(fileName)#for development
                    
            
                if fileTime >= lastCheck:#(unix - fileTime) < 86400:#compare current time to when file was last modified. If modified within last 24hrs(86400 secs) move it to new loc 
                    shutil.move(source+'/'+f, destination)
                    self.txt_moved.insert(1.0, fileName+ '\n')
                    

               # else:
                   # print('{} not changed recently, so it got left where it was.'.format(fileName))
#           #create a label at the bottom that shows how many files were moved
            numMoved=int(self.txt_moved.index('end').split('.')[0])-2
            self.lbl_numMoved=ttk.Label(self.master, text='Number of Files Moved: {}'.format(numMoved))
            self.lbl_numMoved.grid(row=4,column=1, padx=(0,15), pady=(5,0), sticky='e')
            self.txt_choose.delete(0,'end')
            self.txt_dest.delete(0,'end')
            pydrill_table_34_idle.add_to_filemover(self,unix,now)
        else:
            messagebox.showinfo("Cancel Request","No changes will be made")

    elif source == destination:
        messagebox.showerror("Matching Folders","Please choose a destination folder that is different \nfrom the source folder.")
    else:
        messagebox.showerror("Missing Info","Please make sure you choose both a source folder and \na destination folder.")
        
#check_for_updated_files(self,source,destination)
