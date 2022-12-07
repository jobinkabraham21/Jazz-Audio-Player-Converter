from pygame import mixer
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
import moviepy.editor
import os
root=Tk()
root.geometry("339x339")
img= PhotoImage(file='music.png',master= root)
img_label= Label(root,image=img)
img_label.place(x=0, y=0)

root.title('JAZZ AUDIO PLAYER & CONVERTER')


def first_win():
    def playsong():
        currentsong = playlist.get(ACTIVE)
        mixer.music.load(currentsong)
        mixer.music.play()

    def pausesong():
        mixer.music.pause()

    def stopsong():
        mixer.music.stop()

    def resumesong():
        mixer.music.unpause()

    def browse():
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END, song)

    root = Tk()
    root.title('JAZZ AUDIO PLAYER')

    mixer.init()


    playlist = Listbox(root, selectmode=SINGLE, bg="grey", fg="black", font=('arial', 15), width=40)
    playlist.grid(columnspan=5)

    playbtn = Button(root, text="Play", command=playsong)
    playbtn.config(font=('arial', 20), bg="Green", fg="black", padx=7, pady=7)
    playbtn.grid(row=1, column=0)

    pausebtn = Button(root, text="Pause", command=pausesong)
    pausebtn.config(font=('arial', 20), bg="LightBlue", fg="black", padx=7, pady=7)
    pausebtn.grid(row=1, column=1)

    stopbtn = Button(root, text="Stop", command=stopsong)
    stopbtn.config(font=('arial', 20), bg="Red", fg="black", padx=7, pady=7)
    stopbtn.grid(row=1, column=2)

    Resumebtn = Button(root, text="Resume", command=resumesong)
    Resumebtn.config(font=('arial', 20), bg="greenyellow", fg="black", padx=7, pady=7)
    Resumebtn.grid(row=1, column=3)

    openbtn = Button(root, text="Browse", command=browse)
    openbtn.config(font=('arial', 20), bg="Orange", fg="black", padx=7, pady=7)
    openbtn.grid(row=1, column=4)

def second_win():
    root = Tk()
    root.geometry("680x343")
    Label(root, text="Choose a File", bg='red', font=('arial 15')).pack()
    root.title("JAZZ VIDEO TO MP3 CONVERTER")

    def browse():
        global video
        video = askopenfilename()
        video = moviepy.editor.VideoFileClip(video)
        jazz.config(text=video)

    def save():
        audio = video.audio
        audio.write_audiofile("sample.mp3")
        Label(root, text="Video Converted Successfully", bg='blue',font=('arial 15')).pack()

    jazz = Label(root)
    jazz.pack()

    Button(root, text='Browse',bg='orange', command=browse).pack()
    Button(root, text='Save',bg='light blue', command=save).pack()




onebtn=Button(root,text="Audio Player",command=first_win)
onebtn.config(font=('arial',15),bg="green",fg="white",padx=0,pady=0)
onebtn.place(x=10, y=250)

twobtn=Button(root,text="Video to mp3",command=second_win)
twobtn.config(font=('arial',15),bg="red",fg="black",padx=0,pady=0)
twobtn.place(x=185, y=250)

mainloop()
