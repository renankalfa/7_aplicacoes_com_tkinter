import tkinter


class App:

    def __init__(self):

        self.valor = 20

        self.window = tkinter.Tk()
        self.window.title('Marcador')
        self.window.minsize(width=360, height=320)
        self.window.maxsize(width=360, height=320)

        self.text = tkinter.Label(self.window, text=20, font="Arial 80 bold", pady=50)
        self.text.pack()

        self.frame = tkinter.Frame(self.window, bg='white')
        self.frame.pack()

        self.button_plus = tkinter.Button(self.frame, text='Life Potion', bg='green', width=20,
                                          height=4, command=self.plus)
        self.button_plus.pack(side='left')

        self.button_down = tkinter.Button(self.frame, text='Damage', bg='red', width=20,
                                          height=4, command=self.down)
        self.button_down.pack(side='right')

        self.window.mainloop()

    def plus(self):
        if self.valor < 20:
            self.valor += 1
            self.text.config(text=self.valor)

    def down(self):
        if self.valor > 0:
            self.valor -= 1
            self.text.config(text=self.valor)


App()
