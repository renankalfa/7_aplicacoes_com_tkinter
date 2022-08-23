from tkinter import *
import requests
import json

class movieData:

    def __init__(self):

        self.window = Tk()
        self.window.title('Movie Data')
        self.window.geometry('1280x720+300+150')
        self.window.resizable(False, False)

        self.request = requests.get('')
        self.dict = json.loads(self.request.text)

        self.window.mainloop()


movieData()
