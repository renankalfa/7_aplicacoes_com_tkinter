from tkinter import *
import pyscreenshot
from tkinter.colorchooser import askcolor
from tkinter import colorchooser


class Paintk:

    def __init__(self):

        self.window = Tk()
        self.window.title('Paintk')
        self.window.minsize(width=1280, height=720)
        self.window.resizable(False, False)

        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

        self.img_line = PhotoImage(file="icons/line.png")
        self.img_oval = PhotoImage(file='icons/oval.png')
        self.img_eraser = PhotoImage(file='icons/eraser.png')
        self.img_save = PhotoImage(file='icons/save.png')
        self.img_square = PhotoImage(file='icons/square.png')
        self.img_new = PhotoImage(file='icons/new.png')

        self.colors = ("black", "#3b3b3b", "gray", 'white', "red", "green", "blue", "purple", "orange", 'cyan')

        self.pick_colors = 'black'

        self.bar_menu = Frame(self.window, bg='#3b3b3b', height=50)
        self.bar_menu.pack(fill='x')

        self.text_color = Label(self.bar_menu, text='Colors: ', bg='#3b3b3b', fg='white')
        self.text_color.pack(side='left')

        for i in self.colors:
            self.button_color = Button(self.bar_menu, bg=i, width=3, height=2,
                                       command=lambda col=i: self.select_colors(col), bd=0)
            self.button_color.pack(side='left')

        self.label_colors_choose = Label(self.bar_menu, text=' Color Choose: ', fg='white',
                                         bg='#3b3b3b')
        self.label_colors_choose.pack(side='left')

        self.color_choose = Button(self.bar_menu, image=self.img_square, bd=0, command=self.selected_color)
        self.color_choose.pack(side='left')

        self.text_pen_size = Label(self.bar_menu, text=' Size: ', fg='white', bg='#3b3b3b')
        self.text_pen_size.pack(side='left')

        self.pens_size = Spinbox(self.bar_menu, from_=10, to=50, width=5)
        self.pens_size.pack(side='left')

        self.text_brushs = Label(self.bar_menu, text=' Brushs: ', bg='#3b3b3b', fg='white')
        self.text_brushs.pack(side='left')

        self.button_line = Button(self.bar_menu, image=self.img_line, bd=0,
                                    command=self.brush_line)
        self.button_oval = Button(self.bar_menu, image=self.img_oval, bd=0,
                                    command=self.brush_oval)
        self.button_eraser = Button(self.bar_menu, image=self.img_eraser, bd=0,
                                    command=self.brush_eraser)
        self.button_line.pack(side='left')
        self.button_oval.pack(side='left')
        self.button_eraser.pack(side='left')

        self.text_options = Label(self.bar_menu, text='Options: ', bg='#3b3b3b', fg='white')
        self.button_save = Button(self.bar_menu, image=self.img_save, bd=0, command=self.save)
        self.button_new = Button(self.bar_menu, image=self.img_new, bd=0, command=self.clean)
        self.button_save.pack(side='right')
        self.button_new.pack(side='right')
        self.text_options.pack(side='right')

        self.area_draw = Canvas(self.window, height=720, bg='gainsboro')
        self.area_draw.pack(fill='both')
        self.area_draw.bind('<B1-Motion>', self.draw)

        self.window.bind('<F1>', self.clean)

        self.window.mainloop()

    def draw(self, event):
        x1, y1 = event.x, event.y
        x2, y2 = event.x, event.y

        if self.oval_brush:
            self.area_draw.create_oval(x1, y1, x2, y2, fill=self.pick_colors, width=self.pens_size.get(),
                                   outline=self.pick_colors)
        elif self.line_brush:
            self.area_draw.create_line(x1 - 10, y1 - 10, x2, y2, fill=self.pick_colors, width=self.pens_size.get())
        else:
            self.area_draw.create_oval(x1, y1, x2, y2, fill='gainsboro', width=self.pens_size.get(),
                                       outline='gainsboro')

    def select_colors(self, c):
        self.pick_colors = c

    def brush_oval(self):
        self.oval_brush = True
        self.line_brush = False
        self.eraser_brush = False

    def brush_line(self):
        self.oval_brush = False
        self.line_brush = True
        self.eraser_brush = False
        return None

    def brush_eraser(self):
        self.oval_brush = False
        self.line_brush = False
        self.eraser_brush = False

    def clean(self):
        self.area_draw.delete('all')

    def save(self):
        x = self.window.winfo_rootx() + self.area_draw.winfo_x()
        y = self.window.winfo_rooty() + self.area_draw.winfo_y()
        x1 = self.window.winfo_rootx() + self.area_draw.winfo_width()
        y1 = self.window.winfo_rooty() + self.area_draw.winfo_height()

        img = pyscreenshot.grab(bbox=(x, y, x1, y1))
        img.save('image.png', 'png')

    def selected_color(self):
        color = colorchooser.askcolor()
        self.pick_colors = color[1]


Paintk()
