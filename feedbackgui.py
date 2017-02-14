#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:

    def __init__(self, master):    

        master.title('Explore California Feedback')
        master.resizable(False,False)
        master.configure(background='#e1d8b9')
       #style stuff 
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TLabel', text = ('Courier', 11), background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.frame = ttk.Frame(master)
        self.frame.pack(ipadx=3, ipady=3)

       #header 
        self.logo = PhotoImage(file = 'C:\\Users\\Owner\\Desktop\\school projects\\Ex_Files_Python_Tkinter\\Exercise Files\\Ch08\\tour_logo.gif')
        hlabel1 = ttk.Label(self.frame, image = self.logo).grid(row=0, column=0,rowspan=2)
        hlabel2 = ttk.Label(self.frame, font='bold',
                  text='Thank you for choosing the \nDesert to Sea Adventure!').grid(row=0, column=1,)
        hlabel3 = ttk.Label(self.frame, 
                  text='Please leave a comment about your experience.').grid(row=1,column=1)
       

            
       #labels for input fields
        labelName = ttk.Label(self.frame, text='Name:').grid(row=3, column=0, sticky='nw')
        labelEmail = ttk.Label(self.frame, text='E-mail:').grid(row=4, column=0, sticky='nw')
        labelComments = ttk.Label(self.frame, text='Comments:').grid(row=5, column=0, sticky='nw')
       #input fields
        nameVar = StringVar()
        emailVar = StringVar()

        nameEntry = ttk.Entry(self.frame, textvariable=nameVar,
                              width = 49)
        emailEntry = ttk.Entry(self.frame, textvariable=emailVar,
                               width = 49)
        commentsEntry = Text(self.frame, width=37, height=10,
                             wrap='word')
        nameEntry.grid(row=3, column=1, padx=2, pady=2, sticky='w')
        emailEntry.grid(row=4,column=1, padx=2, pady=2, sticky='w')
        commentsEntry.grid(row=5,column=1, rowspan=10, padx=2, pady=2, sticky='w')
        
       #buttons 
        submit = ttk.Button(self.frame, text='Submit', 
                            command = lambda: submitForm(self))
        clearAll= ttk.Button(self.frame, text='Clear All',
                             command = lambda: clearForm())
        submit.grid(row=12, column=0)
        clearAll.grid(row=14, column=0)
        

        def submitForm(self):
            print('Name: {}'.format(nameVar.get()))
            print('Email: {}'.format(emailVar.get()))
            print('Comments: {}'.format(commentsEntry.get(1.0,'end')))
            messagebox.showinfo(title = "Explore California",
                                message = 'Thank you for submitting your comments about \nthe Desert to Sea Adventure!')
            clearForm()

            
        def clearForm(): #clear all the fields
            nameEntry.delete(0,'end')
            emailEntry.delete(0, 'end')
            commentsEntry.delete(1.0, 'end')
        
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()
