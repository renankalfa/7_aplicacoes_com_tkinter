from tkinter import *


class DownTk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Youtube Downloader')
        self.window.resizable(False, False)
        self.window.geometry('1280x720+300+200')

        self.img_logo = PhotoImage(file='assets/logo.png')

        self.frame = Frame(self.window, bg='black')
        self.frame.pack(fill='both')

        self.label_logo = Label(self.frame, image=self.img_logo, bg='black')
        self.label_logo.pack()

        self.window.mainloop()


DownTk()
