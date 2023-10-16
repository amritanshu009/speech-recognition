import tkinter 
from tkinter import filedialog
from tkinter import *

from path import Path
import pyttsx3
from speech_recognition import Recognizer, AudioFile
import speech_recognition as sr
from pydub import AudioSegment
import os
from time import sleep

def takeCommand():
    global showText,go,command
    showText.delete(1.0,"end")
    showText.insert(END,"Listening....")
    
    recog = sr.Recognizer()
    command=''
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"
def stop():
    global go,command
    print("q pressed, exiting...")
    go = 0
    showText.delete(1.0,"end")
    showText.insert(END,command)
def audio_to_text():
    #Creating a window
    global showText
    wn2= tkinter.Tk() 
    wn2.title("TechVidvan Audio to PDF converter")
    wn2.geometry('500x500')
    wn2.config(bg='snow3')
    
    Label(wn2, text='TechVidvan Audio to Text converter',
      fg='black', font=('Courier', 15)).place(x=60, y=10)

    #Getting the PDF path input
    Label(wn2, text='Click the start and end buttons to speak and end speech').place(x=20, y=50)
    
    Button(wn2, text='Start', bg='ivory3',font=('Courier', 13),
       command=takeCommand).place(x=100, y=100)

    #Button to select the audio file and do the conversion 
    Button(wn2, text='Stop', bg='ivory3',font=('Courier', 13),
       command=stop).place(x=200, y=100)
    
    v=Scrollbar(wn2, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    showText=Text(wn2, font=("Calibre, 14"), yscrollcommand=v.set)
    showText.focus()
    showText.place(x=20, y=130,width=450,height=300)
    
    v.config(command=showText.yview)
    wn2.mainloop() #Runs the window till it is closed
#text to voice
voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak():
    global textBox
    text=textBox.get(1.0, "end-1c")
    print(text)
    voiceEngine.say(text)
    voiceEngine.runAndWait()

def text_to_audio():
    #Creating a window 
    global textBox
    wn1 = tkinter.Tk() 
    wn1.title("TechVidvan Text to Audio converter")
    wn1.geometry('500x500')
    wn1.config(bg='snow3')
    
    Label(wn1, text='TechVidvan Text to Audio converter',
      fg='black', font=('Courier', 15)).place(x=60, y=10)
    
    v=Scrollbar(wn1, orient='vertical')
    v.pack(side=RIGHT, fill='y')
    textBox=Text(wn1, font=("Calibre, 14"), yscrollcommand=v.set)
    textBox.focus()
    textBox.place(x=20, y=80,width=450,height=300)
    
    v.config(command=textBox.yview)
    Button(wn1, text="Convert", bg='ivory3',font=('Courier', 13),
       command=speak).place(x=230, y=400)
    
    wn1.mainloop()
wn = tkinter.Tk() 
wn.title("PythonGeeks Text to Audio and Audio to Text converter")
wn.geometry('700x300')
wn.config(bg='LightBlue1')
  
Label(wn, text='TechVidvan Text to Audio and Audio to Text converter',
      fg='black', font=('Courier', 15)).place(x=40, y=10)

global textBox,showText,command,go
go=1

Button(wn, text="Convert Text to Audio", bg='ivory3',font=('Courier', 15),
       command=text_to_audio).place(x=230, y=80)
Button(wn, text="Convert Audio to Text", bg='ivory3',font=('Courier', 15),
       command=audio_to_text).place(x=230, y=150)

wn.mainloop()
