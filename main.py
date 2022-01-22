import time
from tkinter import *

def click():
    print('hellow rold')

windows=Tk()

entry=Entry(windows,
            font=("Arial",50),
            show='*'
            )
entry.pack()
submit_button=Button(windows,text='submit',command='submit',state=ACTIVE)

submit_button.pack()

windows.mainloop()


