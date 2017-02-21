from tkinter import *
from tkinter import ttk
import os
import pydrill_scripting_27_idle
import pydrill_gui_34_idle
import sqlite3
from datetime import datetime
import time

def create_db(self):
    conn=sqlite3.connect('filemover.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_filemover( \
                    col_fileCheck FLOAT, \
                    col_fileCheckDate DATETIME \
                    );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):#puts info into the table for the first time. sets the initial time for the lastCheck as 24hrs before program is first run
    now=datetime.now()#get current time
    unix=time.mktime(now.timetuple())#change current time to unix time
    firstTime=(unix-86400)#sets the first value in the filemover table to 24hrs ago for the first check
    firstCheck=datetime.fromtimestamp(firstTime)
    conn=sqlite3.connect('filemover.db')
    with conn:
        cur=conn.cursor()
        cur,count=count_records(cur)
        if count<1:
            cur.execute("""INSERT INTO tbl_filemover
                        (col_fileCheck,col_fileCheckDate) VALUES (?,?)""",(firstTime,firstCheck,))
            conn.commit()
    conn.close()
    

def count_records(cur):
    count=""
    cur.execute("""select count (*) FROM tbl_filemover""")
    count=cur.fetchone()[0]
    return cur,count

def add_to_filemover(self,unix,now):#adds a record to the table everytime a check is performed
    lastCheckUnix=unix
    lastCheckDate=now
    conn=sqlite3.connect('filemover.db')
    with conn:
        cur=conn.cursor()
        cur.execute("""INSERT INTO tbl_filemover
                    (col_fileCheck, col_fileCheckDate) VALUES (?,?)""",(lastCheckUnix,lastCheckDate,))
        conn.commit()
    conn.close
    self.txt_lastCheck.delete(0, 'end')
    self.txt_lastCheck.insert(0, lastCheckDate)
                    
