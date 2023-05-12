from tkinter import *
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader")
root.geometry("700x350")
root.resizable(0,0)
root.config(bg="orange")

Label(root, text="Download Youtube video for free", font="Arial 14 bold").place(x=100,y=20)
Label(root, text="Paste your youtube link", font="Arial 14", bg="cyan",fg="white").place(x=120,y=50)

videoLink = StringVar()
Entry(root,width=80,textvariable=videoLink).place(x=35,y=85)

def download():
    url=YouTube(str(videoLink.get()))
    videoStream = url.streams.first()
    videoStream.download("/home/bharathi/")
    Label(root,text="Downloaded Successfully",font="Arial 16 bold",bg="red",fg="white").place(x=120,y=180)

Button(root,text="Download Now",command=download,font="Arial 16 bold",bg="red",padx=2).place(x=180,y=120)

root.mainloop()