from tkinter import *


class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title('Calculadora')
        self.window.resizable(False, False)


        # Visor de números
        self.screen_numbers = Entry(self.window, font='Arial 20 bold', bg='#172d36',
                                    fg='white', width=16)
        self.screen_numbers.pack()


        self.frame = Frame(self.window)
        self.frame.pack()

        # Adicionando os botões
        self.button_1 = Button(self.frame, bg='orange', text=1, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('1'), fg='white')

        self.button_2 = Button(self.frame, bg='orange', text=2, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('2'), fg='white')

        self.button_3 = Button(self.frame, bg='orange', text=3, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('3'), fg='white')

        self.button_4 = Button(self.frame, bg='orange', text=4, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('4'), fg='white')

        self.button_5 = Button(self.frame, bg='orange', text=5, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('5'), fg='white')

        self.button_6 = Button(self.frame, bg='orange', text=6, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('6'), fg='white')

        self.button_7 = Button(self.frame, bg='orange', text=7, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('7'), fg='white')

        self.button_8= Button(self.frame, bg='orange', text=8, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('8'), fg='white')

        self.button_9 = Button(self.frame, bg='orange', text=9, bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('9'), fg='white')

        self.button_add = Button(self.frame, bg='orange', text='+', bd=0,
                               font='Arial 20 bold', width=3, height=1,
                               command=lambda: self.touch('+'), fg='white')

        self.button_sub = Button(self.frame, bg='orange', text='-', bd=0,
                                 font='Arial 20 bold', width=3, height=1,
                                 command=lambda: self.touch('-'), fg='white')

        self.button_division = Button(self.frame, bg='orange', text='/', bd=0,
                                 font='Arial 20 bold', width=3, height=1,
                                 command=lambda: self.touch('/'), fg='white')

        self.button_multi = Button(self.frame, bg='orange', text='x', bd=0,
                                 font='Arial 20 bold', width=3, height=1,
                                 command=lambda: self.touch('*'), fg='white')

        self.button_equal = Button(self.frame, bg='orange', text='=', bd=0,
                                 font='Arial 20 bold', width=3, height=1,
                                 command=self.total, fg='white')

        self.button_clean = Button(self.frame, bg='orange', text='C', bd=0,
                                 font='Arial 20 bold', width=3, height=1,
                                 command=self.Clean, fg='white')

        self.button_dot = Button(self.frame, bg='orange', text=',', bd=0,
                                   font='Arial 20 bold', width=3, height=1,
                                   command=lambda: self.touch(','), fg='white')

        self.button_1.grid(row=0, column=0, padx=1, pady=1)
        self.button_2.grid(row=0, column=1, padx=1, pady=1)
        self.button_3.grid(row=0, column=2, padx=1, pady=1)
        self.button_clean.grid(row=0, column=3, padx=2, pady=1)
        self.button_4.grid(row=1, column=0, padx=1, pady=1)
        self.button_5.grid(row=1, column=1, padx=1, pady=1)
        self.button_6.grid(row=1, column=2, padx=1, pady=1)
        self.button_multi.grid(row=1, column=3, padx=2, pady=1)
        self.button_7.grid(row=2, column=0, padx=1, pady=1)
        self.button_8.grid(row=2, column=1, padx=1, pady=1)
        self.button_9.grid(row=2, column=2, padx=1, pady=1)
        self.button_division.grid(row=2, column=3, padx=2, pady=1)
        self.button_equal.grid(row=3, column=3, padx=1, pady=1)
        self.button_add.grid(row=3, column=2, padx=1, pady=1)
        self.button_sub.grid(row=3, column=1, padx=1, pady=1)
        self.button_dot.grid(row=3, column=0, padx=1, pady=1)



        self.window.mainloop()

    def touch(self, num):
        self.screen_numbers.insert(END, num)

    def Clean(self):
        self.screen_numbers.delete(0, END)

    def total(self):
        valor = eval(self.screen_numbers.get())
        self.screen_numbers.delete(0, END)
        self.screen_numbers.insert(0, str(valor))

Calc()
