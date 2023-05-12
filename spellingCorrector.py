from tkinter import *
from textblob import TextBlob

root = Tk()
root.configure(background="greenyellow")
root.geometry("750x350")
root.resizable(0,0)
root.title("Spell Checker and Corrector App")

headingText = Label(root,text="Spell Checker And Corrector", font="Arial 16 bold",fg="yellow",bg="black")
lblInput = Label(root,text="Input Word", font="Arial 16 bold",fg="white",bg="magenta")
lblCorrected = Label(root,text="Corrected Word", font="Arial 16 bold",fg="white",bg="green")

headingText.grid(row=0,column=1,padx=20)
lblInput.grid(row=1,column=0,padx=10)
lblCorrected.grid(row=3,column=0,padx=10)


inputWordBox = Entry(root,width=40,font="Arial 16 bold")
correctedWordBox = Entry(root,width=40,font="Arial 16 bold")

inputWordBox.grid(row=1,column=1,pady=10)
correctedWordBox.grid(row=3,column=1,pady=10)

def spellCorrection():
    wordInput = inputWordBox.get()
    text = TextBlob(wordInput)

    correctedWord = str(text.correct())

    correctedWordBox.insert(10,correctedWord)

def clearAll():
    inputWordBox.delete(0,END)
    correctedWordBox.delete(0,END)

btn1 = Button(root,text="Correction",font="Arial 16 bold",fg="white",bg="aqua",border=5,command=spellCorrection)
btn1.grid(row=2,column=1)

btn1 = Button(root,text="Clear All",font="Arial 16 bold",fg="black",bg="red",border=5,command=clearAll)
btn1.grid(row=4,column=1)

root.mainloop()