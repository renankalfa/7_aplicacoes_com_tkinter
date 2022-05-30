from tkinter import *


class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Paintk')
        self.window.minsize(width=1280, height=720)
        self.window.resizable(False, False)

        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill='x')

        self.text_color = Label(self.bar_menu, text='Colors: ', bg='#3b3b3b', fg='white')
        self.text_color.pack(side='left')

        self.button_color = Button(self.bar_menu, bg='black', width=3, height=2,
                                   command=None, bd=0)
        self.button_color.pack(side='left')

        self.area_draw = Canvas(self.window, height=720)
        self.area_draw.pack(fill='both')

        self.window.mainloop()


Paintk()
