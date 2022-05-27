import tkinter


def NewFile():
    print('Crie um novo arquivo')


def SaveFile():
    print('Salvo um novo arquivo')


def Save_as():
    print('Salvar como')


# Gerar a janela
window = tkinter.Tk()
window.title('Notepad')
window.geometry('1280x720')
window.minsize(width=1280, height=720)

# Criar uma área de texto
text_area = tkinter.Text(window, font='Arial 20 bold', width=1280, height=720)
text_area.pack()

# Criar um menu de opções
main_menu = tkinter.Menu(window)

## Criando um menu dentro de outro menu
file_menu = tkinter.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New', command=NewFile)
file_menu.add_command(label='Save', command=SaveFile)
file_menu.add_command(label='Save as ...', command=Save_as)
file_menu.add_command(label='Exit', command=window.quit)

main_menu.add_cascade(label='File', menu=file_menu)
window.config(menu=main_menu)

# Cria um loop para deixar a janela aberta
window.mainloop()
