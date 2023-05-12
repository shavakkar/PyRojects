from tkinter import *
import datetime
from PIL import Image
from PIL import ImageTk

root =Tk()
root.geometry("650x750")
root.title("Age Calculator")
root.resizable(0,0)

name = Label(root,text="Name")
name.place(x=200,y=300)
year = Label(root,text="Year")
year.place(x=200,y=350)
month = Label(root,text="Month")
month.place(x=200,y=400)
day = Label(root,text="Day")
day.place(x=200,y=450)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=25, font="Arial 14")
nameEntry.place(x=250,y=300)
yearEntry = Entry(root, textvariable=yearValue, width=25, font="Arial 14")
yearEntry.place(x=250,y=350)
monthEntry = Entry(root, textvariable=monthValue, width=25, font="Arial 14")
monthEntry.place(x=250,y=400)
dayEntry = Entry(root, textvariable=dayValue, width=25, font="Arial 14")
dayEntry.place(x=250,y=450)

def userInput():
    name = nameEntry.get()
    hero = Person(name,datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get())))
    textArea = Text(master=root,height=5,width=35,bg="pink",font="Arial 14")
    textArea.place(x=200,y=550)
    answer = 'Hello {hero}!!!. You are {age} Years old!'.format(hero=name, age=hero.age())
    textArea.insert(END,answer)

button = Button(root, text="calculate Age", bg="red", font="Arial 16", command=userInput)
button.place(x=300,y=500)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

image = Image.open('bar-code.png')
image.thumbnail((500,200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
imageLabel = Label(image=photo)
imageLabel.place(x=220,y=60)

root.mainloop()