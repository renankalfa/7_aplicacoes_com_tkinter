from tkinter import *
import youtube_dl
import os
from tkinter import filedialog

class DownTk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(False, False)
        self.window.geometry('1280x720+300+200')

        self.img_logo = PhotoImage(file='assets/logo.png')

        self.audio = False
        self.video = False

        self.frame = Frame(self.window, bg='#3b3b3b', pady=80)
        self.frame.pack(fill='x')

        self.label_logo = Label(self.frame, image=self.img_logo, bg='#3b3b3b')
        self.label_logo.pack()

        self.frame2 = Frame(self.window, pady=20)
        self.frame2.pack()

        self.label_insert = Label(self.frame2, text='  Insert Link:  ', font='arial 12 bold')
        self.label_insert.pack(side='left')

        self.link = Entry(self.frame2, font='arial 20', width=42)
        self.link.pack(side='left')

        self.play = Button(self.frame2, bg='red', text='>', bd=0, fg='white',
                           command=lambda: self.download(self.link.get())
                           , width=5, height=2)
        self.play.pack()

        self.ab = lambda : self.download(self.link.get())
        print(self.ab)

        self.frame3 = Frame(self.window)
        self.frame3.pack()

        self.radio1 = Radiobutton(self.frame3, text='Audio', value=0, command=self.validate_audio)
        self.radio1.pack(side='left')

        self.radio2 = Radiobutton(self.frame3, text='Vídeo', value=1, command=self.validate_video)
        self.radio2.pack(side='left')

        self.radio3 = Radiobutton(self.frame3, text='Both', value=2, command=self.validate_both)
        self.radio3.pack(side='left')

        self.window.mainloop()

    def validate_audio(self):
        self.audio = True
        self.video = False

    def validate_video(self):
        self.audio = False
        self.video = True

    def validate_both(self):
        self.audio = False
        self.video = False

    def download(self, link):
        os.system('youtube-dl ' + str(link))
        self.complete()

    def mensage(self):
        window = Toplevel()
        window.title('E R R O')
        window.resizable(False, False)
        window.geometry('300x200')

        text = Label(window, text='O link não é valido', font='arial 20 bold', pady=30)
        text.pack()

        button_exit = Button(window, text='  OK  ', command=window.destroy)
        button_exit.pack()

    def complete(self):
        window = Toplevel()
        window.title('Efetuado')
        window.resizable(False, False)

        text = Label(window, text='Download Efetuado', pady=30)
        text.pack()

        button_exit = Button(window, text='  OK  ', command=window.destroy)
        button_exit.pack()


DownTk()
