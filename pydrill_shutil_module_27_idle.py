#This is a practice drill for Tech Academy Python Course item 63 drill.
#The purpose is to move files from one folder to another.
#Author:Matt Thoman

import shutil, os

source = "C:\\Users\\Owner\Desktop\\File Alpha\\"#set where files are that you want moved
destination = "C:\\Users\\Owner\\Desktop\\File Bravo\\"#set where you want them to go

for f in os.listdir(source):
    if f.endswith('.txt'):
        shutil.move(source+f, destination)

print('Files Moved')

