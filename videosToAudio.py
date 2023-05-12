import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog

def convert():
    videoclip = mp.VideoFileClip(fname)
    videoclip.audio.write_audiofile("hello.mp3")
    messageToGenerate.set("Success!")

def upload():
    filename = filedialog.askopenfilename(filetypes=[('Mp4 Files', '*mp4'),('WMV Files', '*.wmv'),('ogg files', '*.ogg')])
    messageForUpload.set("File Uploaded: "+filename)
    global fname 

    fname = filename

root = Tk()

root.geometry("700x250")
root["bg"] = "orange"
root.title("video to audio app")

global messageForUpload
global messageToGenerate

messageForUpload = StringVar()
messageToGenerate = StringVar()

Label(root,text="hello",textvar=messageForUpload, font="Arial 12",fg="white",bg="orange").place(x=100,y=40)

Button(root,text="Upload Video",command=upload, font="Arial 12",fg="white",bg="orange").place(x=100,y=70)

Button(root,text="Convert Video",command=convert, font="Arial 12 bold",fg="white",bg="orange").place(x=300,y=70)

Label(root,text="hello",textvar=messageToGenerate, font="Arial 12",fg="white",bg="orange").place(x=100,y=120)

root.mainloop()