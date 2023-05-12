from tkinter import *
import pyspeedtest

app = Tk()
app.configure(background="greenyellow")
app.geometry("750x350")
app.resizable(0,0)
app.title("Internet Speed Tester")

pingSpeed = StringVar()
downSpeed = StringVar()

headingText = Label(app, text="Internet Speed Tester", font="Arial 16 bold",fg="yellow",bg="black")
webUrl = Label(app, text="Enter Web URL", font="Arial 14 bold",fg="white",bg="blue")
pingResult = Label(app, text="Ping Result", font="Arial 16 bold",fg="yellow",bg="red")
downloadResult = Label(app, text="Download Result", font="Arial 16 bold",fg="white",bg="purple")

headingText.grid(row=0,column=1,pady=20)
webUrl.grid(row=1,column=0,padx=10)
pingResult.grid(row=3,column=0,padx=10)
downloadResult.grid(row=4,column=0,padx=10,pady=10)

result1 = Label(app, text=" ",textvariable=pingSpeed, font="Arial 14 bold",fg="white",bg="black")
result1.grid(row=3,column=1)
result2 = Label(app, text=" ",textvariable=downSpeed, font="Arial 14 bold",fg="yellow",bg="black")
result2.grid(row=4,column=1)

urlEntery = Entry(app,width=25,font="Arial 14 bold")
urlEntery.grid(row=1,column=1)

def speedTest():
    internet = pyspeedtest.SpeedTest(urlEntery.get())
    pingSpeed.set(internet.ping())
    downSpeed.set(internet.download())

btn = Button(app,text="Check Speed Here", font="Arial 14 bold",fg="black",bg="aqua",command=speedTest)
btn.grid(row=2,column=1,pady=10)

app.mainloop()