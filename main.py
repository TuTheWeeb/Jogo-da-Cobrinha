from constantes import *
#import elementos as el
#import mapa as map
#import numpy as np
#from random import choice
#import integracao as integ
from tkinter import *
from PIL import ImageTk, Image

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
        #self.Menu.grid(row=0, column=0, sticky="nsew")
        #self.Jogo.grid(row=0, column=0, sticky="nsew")
        #self.GameOver.grid(row=0, column=0, sticky="nsew")
        self.Menu.pack(fill="both", expand=True)
        self.Jogo.pack(fill="both", expand=True)
        self.GameOver.pack(fill="both", expand=True)
        self.menu()

    def menu(self):
        self.Menu.tkraise()
        self.nome = Label(self.Menu, text="Jogo da Cobrinha!")
        self.nome.pack(pady=10)

        self.botao_inciar = Button(self.Menu, text="Jogar", command=self.jogar)
        self.botao_inciar.pack(pady=GAME_HEIGHT//3, side="left")

        self.botao_sair = Button(self.Menu, text="Sair", command=self.master.destroy)
        self.botao_sair.pack(pady=GAME_HEIGHT//3, side="right")

    def jogar(self):
        pass




if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


