from tkinter import *


class DownTk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(False, False)
        self.window.geometry('1280x720+300+200')

        self.img_logo = PhotoImage(file='assets/logo.png')

        self.frame = Frame(self.window, bg='#3b3b3b')
        self.frame.pack()

        self.window.mainloop()


DownTk()
