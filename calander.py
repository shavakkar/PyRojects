from tkcalendar import Calendar
from tkinter import *

root =Tk()

root.geometry("420x420")
root.title("Calendar")
root.config(background="orange")

calenderObj = Calendar(root,selectmode="day",year=2022,month=1,date=1)

calenderObj.pack(pady=45)

def fetchDate():
    date.config(text="Selected Date is: "+ calenderObj.get_date())

button = Button(root,text="Select Date",bg="black",fg="white",command=fetchDate)
button.pack()

date = Label(root,text="",bg="black",fg="white")
date.pack(pady=20)

root.mainloop()