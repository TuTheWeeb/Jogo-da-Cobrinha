from constantes import *
#import elementos as el
#import mapa as map
#import numpy as np
#from random import choice
#import integracao as integ
from tkinter import *

class App():
    def __init__(self, master=None):
        """
        Define as caracteristicas da Applicação
        """
        # Definições
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Jogo da Cobrinha")
        self.master.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")

        # Cria as paginas ou Frames
        self.Menu = Frame(self.master)
        self.Jogo = Frame(self.master)
        self.GameOver = Frame(self.master)

        # Coloca as paginas em modelo grid
        self.Menu.grid(row=0, column=0)
        self.Jogo.grid(row=0, column=0)
        self.GameOver.grid(row=0, column=0)

        self.menu()

    def menu(self):
        self.Menu.tkraise()
        self.title = Label(self.Menu, text="Jogo da Cobrinha")
        self.title.pack()


if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


