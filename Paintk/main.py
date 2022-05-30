from tkinter import *


class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Paintk')
        self.window.minsize(width=1280, height=720)
        self.window.resizable(False, False)

        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file='icons/oval.png')
        self.img_eraser = PhotoImage(file='icons/eraser.png')
        self.img_save = PhotoImage(file='icons/save.png')
        self.img_square = PhotoImage(file='icons/square.png')
        self.img_new = PhotoImage(file='icons/new.png')

        self.colors = ("black", "#3b3b3b", "gray", "white", "red", "green", "blue", "purple", "orange", 'cyan')

        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill='x')

        self.text_color = Label(self.bar_menu, text='Colors: ', bg='#3b3b3b', fg='white')
        self.text_color.pack(side='left')

        for i in self.colors:
            self.button_color = Button(self.bar_menu, bg=i, width=3, height=2,
                                       command=None, bd=0)
            self.button_color.pack(side='left')

        self.text_pen_size = Label(self.bar_menu, text='Size: ', fg='white', bg='#3b3b3b')
        self.text_pen_size.pack(side='left')

        self.pens_size = Spinbox(self.bar_menu, from_=1, to=50)
        self.pens_size.pack(side='left')

        self.text_brushs = Label(self.bar_menu, text='Brushs: ', bg='#3b3b3b', fg='white')
        self.text_brushs.pack(side='left')

        self.button_line = Button(self.bar_menu, image=self.img_line, bd=0)
        self.button_oval = Button(self.bar_menu, image=self.img_oval, bd=0)
        self.button_eraser = Button(self.bar_menu, image=self.img_eraser, bd=0)
        self.button_line.pack(side='left')
        self.button_oval.pack(side='left')
        self.button_eraser.pack(side='left')

        self.text_options = Label(self.bar_menu, text='Options: ', bg='#3b3b3b', fg='white')
        self.text_options.pack(side='left')

        self.button_save = Button(self.bar_menu, image=self.img_save, bd=0)
        self.button_new = Button(self.bar_menu, image=self.img_new, bd=0)
        self.button_save.pack(side='left')
        self.button_new.pack(side='left')


        self.area_draw = Canvas(self.window, height=720)
        self.area_draw.pack(fill='both')

        self.window.mainloop()


Paintk()
