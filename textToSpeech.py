import pyttsx3
import os

voice = pyttsx3.init()
text = "Hello Everyone!"
voice.say(text)
voice.save_to_file(text, "hello.mp3")
voice.runAndWait()
os.system("start hello.mp3")
