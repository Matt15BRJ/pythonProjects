#Python 3.6.0
#Purpose: Create a GUI to let users choose a folder to check for updated .txt files
#           and move any updated files to a noew folder of the users choice
#Author: Matt Thoman

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import os

import pydrill_scripting_27_idle
import pydrill_table_34_idle

class ParentWindow(Frame):
    def __init__(self,master, *args, **kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.master=master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)
        self.master.resizable(False,False)

        self.master.title('Check for updated files')
        self.master.protocol('WM_DELETE_WINDOW', lambda: ask_quit(self))
        arg=self.master
        pydrill_table_34_idle.create_db(self)
        

    
        def load_gui(self):
            #labels
            self.lbl_choose=ttk.Label(self.master, text='Choose a folder to check for \nnew or modified files.')
            self.lbl_choose.grid(row=0,column=0, padx=(15,0), pady=(5,0),sticky='w')
            self.lbl_dest=ttk.Label(self.master, text='Choose a destination folder \nfor new or modified files.')
            self.lbl_dest.grid(row=0,column=1, padx=(0,15), pady=(5,5),sticky='e')
            self.lbl_moved=ttk.Label(self.master, text='Files Moved')
            self.lbl_moved.grid(row=4,column=0, padx=(15,0), pady=(5,0),sticky='w')
            self.lbl_lastCheck=ttk.Label(self.master, text='Last check performed:')
            self.lbl_lastCheck.grid(row=6,column=0, padx=(15,0), pady=(5,5), sticky='w')
            #select folder buttons 
            self.btn_choose=ttk.Button(self.master, text='Browse', command= lambda: browse_file_choose(self))
            self.btn_choose.grid(row=1,column=0, padx=(15,0),pady=(5,5),sticky='w')
            self.btn_dest=ttk.Button(self.master, text='Browse', command= lambda: browse_file_dest(self))
            self.btn_dest.grid(row=1,column=1, padx=(0,15), pady=(5,5),sticky='e')
            #display selected file paths
            self.txt_choose=ttk.Entry(self.master, width=40, text='')
            self.txt_choose.grid(row=2,column=0, padx=(15,5), pady=(5,5), sticky='w')
            self.txt_dest=ttk.Entry(self.master, width=40, text='')
            self.txt_dest.grid(row=2,column=1, padx=(5,15), pady=(5,5),sticky='e')
            
           
            
            #buttons
            self.btn_submit=ttk.Button(self.master, text='Begin Check', command=lambda: pydrill_scripting_27_idle.check_for_updated_files(self))
            self.btn_submit.grid(row=3,column=0, padx=(15,0),pady=(5,5),sticky='w')
            self.btn_clearAll=ttk.Button(self.master, text='Clear All', command=lambda: clearAll(self))
            self.btn_clearAll.grid(row=3,column=1, padx=(0,15),pady=(5,5), sticky='e')
            #display any moved files
            self.scrollbar1=Scrollbar(self.master, orient=VERTICAL)
            self.txt_moved=Text(self.master, width=70, height=10, yscrollcommand=self.scrollbar1.set)
            self.txt_moved.grid(row=5, column=0, columnspan=2, padx=(15,15), pady=(5,10), sticky=NSEW)
            self.txt_lastCheck=ttk.Entry(self.master, width=30, text='')
            self.txt_lastCheck.grid(row=6,column=0, columnspan=2, padx=(140,0), pady=(5,5), sticky='w')
            
            #scrollbar for list of moved files
            
            self.scrollbar1.config(command=self.txt_moved.yview)
            self.scrollbar1.grid(row=5,column=0,columnspan=1,padx=(15,15), pady=(5,10), sticky=N+E+W)

            #populate lastCheck box with the date/time of the last time the program was run
            conn=sqlite3.connect('filemover.db')
            with conn:
                cur=conn.cursor()
                cur.execute("""SELECT max(col_fileCheckDate) FROM tbl_filemover""")
                lastCheckDate=cur.fetchone()[0]
                self.txt_lastCheck.delete(0, 'end')
                self.txt_lastCheck.insert(0, lastCheckDate)
                conn.commit()
            conn.close()




        def browse_file_choose(self):#bring up file browser, insert folder path into entry box
            currdir=os.getcwd()
            source=filedialog.askdirectory(initialdir=currdir)
            self.txt_choose.delete(0,'end')
            self.txt_choose.insert(0, source)
            #print(source)#for development
            
        def browse_file_dest(self):#bring up file browser, insert folder path into entrybox
            currdir=os.getcwd()
            destination=filedialog.askdirectory(initialdir=currdir)
            self.txt_dest.delete(0,'end')
            self.txt_dest.insert(0, destination)
            #print(destination)#for development
            
        
        def clearAll(self):#clears all of the fields
            self.txt_choose.delete(0,'end')
            self.txt_dest.delete(0,'end')
            self.txt_moved.delete(1.0,'end')
            self.lbl_numMoved.grid_forget()


        def ask_quit(self):
            if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
                #this closes app
                self.master.destroy()
                os._exit(0)#cleans all the widgets, etc from this program out of the
                #users memory to free up space and eliminate any possible memory leaks

        
        load_gui(self)




if __name__=="__main__":
    root=Tk()
    App=ParentWindow(root)
    root.mainloop()
