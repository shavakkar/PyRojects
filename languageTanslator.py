from tkinter import *
from translate import Translator

screen = Tk()

screen.title("language translator")
screen.geometry("630x750")
screen.resizable(0,0)
screen.config(bg="orange")

InputLanguageChoice = StringVar()
InputLanguageChoice.set("English")
LanguageChoices = OptionMenu(screen,InputLanguageChoice,'Hindi','English','French','German','Spanish')
LanguageChoices.config(bg="green", fg="white")
LanguageChoices["menu"].config(bg="red")
LanguageChoices.grid(row=2,column=2,pady=10,ipadx=15)

OutputLanguageChoice = StringVar()
OutputLanguageChoice.set("English")
LanguageChoices = OptionMenu(screen,OutputLanguageChoice,'Hindi','English','French','German','Spanish')
LanguageChoices.config(bg="green", fg="white")
LanguageChoices["menu"].config(bg="red")
LanguageChoices.grid(row=2,column=4,ipadx=15)

Label(screen, text="Enter text here").grid(row=3,column=1)
textVar = StringVar()
textbox = Entry(screen, textvariable=textVar).grid(row=3,column=2,ipadx=15,pady=20)

Label(screen, text="Output text").grid(row=3,column=3)
outVar = StringVar()
textbox = Entry(screen, textvariable=outVar).grid(row=3,column=4,ipadx=15,pady=20)

def translate():
    translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=OutputLanguageChoice.get())
    translation = translator.translate(textVar.get())
    outVar.set(translation)

B = Button(screen, text="Translate",command=translate, relief=GROOVE).grid(row=4,column=3)

screen.mainloop()