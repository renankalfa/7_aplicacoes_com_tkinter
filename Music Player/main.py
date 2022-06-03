from tkinter import *


class Music_Player:

    def __init__(self):

        self.window = Tk()
        self.window.title('Music Player')
        self.window.resizable(False, False)
        self.window.geometry('300x400+800+300')
        self.window.mainloop()


Music_Player()
