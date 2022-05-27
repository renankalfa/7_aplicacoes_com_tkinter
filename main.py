import tkinter

# Gerar a janela
window = tkinter.Tk()
window.title('Notepad')
window.geometry('1280x720')
window.minsize(width=1280, height=720)

#
text_area = tkinter.Text(window, font='Arial 20 bold')
text_area.pack()

main_menu = tkinter.Menu(window)
main_menu.add_cascade(label='File')
window.config(menu=main_menu)

window.mainloop()
