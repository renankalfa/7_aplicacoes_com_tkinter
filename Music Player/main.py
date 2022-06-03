from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk


class Music_Player:

    def __init__(self):

        self.window = ThemedTk(theme='black')
        self.window.title('Music Player')
        self.window.resizable(False, False)
        self.window.geometry('300x400+800+300')
        self.window.config(bg='#333333')

        self.list = Listbox(self.window, bg='#444444', height=16)
        self.list.pack(fill='x', padx=10, pady=10)

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)

        self.remove = ttk.Button(self.frame)
        self.remove.grid(row=0, column=0)

        self.add = ttk.Button(self.frame)
        self.add.grid(row=0, column=1)

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=10)

        self.previus = ttk.Button(self.frame2)
        self.previus.grid(row=0, column=0)

        self.play = ttk.Button(self.frame2)
        self.play.grid(row=0, column=1)

        self.next = ttk.Button(self.frame2)
        self.next.grid(row=0, column=3)


        self.window.mainloop()


Music_Player()
