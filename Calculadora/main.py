from tkinter import *

# Teste github

class Calc:

    def __init__(self):

        self.window = Tk()
        self.window.title('Calculadora')
        self.window.resizable(False, False)


        # Visor de números
        self.screen_numbers = Entry(self.window, font='Arial 20 bold', bg='#172d36', fg='white')
        self.screen_numbers.pack()


        self.frame = Frame(self.window)
        self.frame.pack()

        # Adicionando os botões
        self.button_1 = Button(self.frame, bg='orange', text='1', bd=0, font='Arial 20 bold',
                               width=5, height=3)
        self.button_1.grid(row=0, column=0)

        self.window.mainloop()

Calc()
