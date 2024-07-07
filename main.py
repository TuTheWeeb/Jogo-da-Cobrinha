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
        """Cria a janela do menu inicial"""
        self.Menu.tkraise()
        self.nome = Label(self.Menu, text="Jogo da Cobrinha!")
        self.nome.pack(pady=10)

        fonte_botao=("Comic Sans", 15)
        self.botao_inciar = Button(self.Menu, text="Jogar", font=fonte_botao, height= 5, width=20, background= "#e361f4", command=self.jogar)
        self.botao_inciar.pack(pady=GAME_HEIGHT//3, side="bottom")

        self.botao_sair = Button(self.Menu, text="Sair", command=self.master.destroy)
        self.botao_sair.pack(pady=GAME_HEIGHT//3, side="top")

    def jogar(self): #nao ta funcionando como comando do botao
        score = 0
        self.Jogo.tkraise()

        #Label de pontuação
        label = Label(self.Jogo, text="Score: {}".format(score),font=("consolas", 40))
        label.pack()

        #Criação da canvas 
        canvas = Canvas(self.Jogo, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        canvas.pack()

        
if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


