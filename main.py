from constantes import *
import elementos as el
from mapa import Mapa
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
        self.master.config(height=GAME_HEIGHT, width=GAME_WIDTH)
        self.master.resizable(False, False)
        self.master.title("Jogo da Cobrinha")
        self.master.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")

        # Cria as paginas ou Frames
        self.Menu = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.Jogo = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.GameOver = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)

        # Coloca as paginas em modelo grid
        self.Menu.grid(row=0, column=0, sticky="nsew")
        self.Jogo.grid(row=0, column=0, sticky="nsew")
        self.GameOver.grid(row=0, column=0, sticky="nsew")

        self.menu()

    def menu(self):
        """Cria a janela do menu inicial"""

        background_image = Image.open('Cobra.jpg')
        background_image = ImageTk.PhotoImage(background_image)

        fonte=("Comic Sans", 15)

        self.Menu.tkraise()

        menu_canvas = Canvas(self.Menu, width=GAME_WIDTH, height=GAME_HEIGHT)
        menu_canvas.background_image = background_image
        menu_canvas.create_image(0, 0, anchor=NW, image=background_image)
        menu_canvas.place(x=0,y=0)

        self.nome = Label(self.Menu, text="Jogo da Cobrinha!", font=fonte)
        self.nome.place(x=(GAME_WIDTH//2 - 90), y=10)

        y_botao = 0.6

        self.botao_inciar = Button(self.Menu, text="Jogar", font=fonte, height=2, width=10, command=self.jogar)
        self.botao_inciar.place(relx=0.3, rely=y_botao, anchor=CENTER)

        self.botao_sair = Button(self.Menu, text="Sair", font=fonte, height=2, width=10, command=self.master.destroy)
        self.botao_sair.place(relx=0.7, rely=y_botao, anchor=CENTER)

    def jogar(self):
        self.Jogo.tkraise()
        self.score = 0

        #Label de pontuação
        self.label = Label(self.Jogo, text="Score: {}".format(self.score), font=("consolas", 40))
        self.label.pack()

        #Criação da canvas 
        self.canvas = Canvas(self.Jogo, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()

        self.lista_elementos = []
        self.Mapa = Mapa()
        self.renderizar()

    def addicionar_obj(self, obj):
        self.lista_elementos.append(obj)
    def renderizar(self):
        self.Mapa.gerar_fruta()
        for row in self.Mapa.matriz:
            for column in row:
                if column.nome == "QuadradoVazio": continue

                self.addicionar_obj(
                    self.canvas.create_rectangle(
                        column.coordenadas[0]*WIDTH_PROPORTIONS,
                        column.coordenadas[1]*HEIGHT_PROPORTIONS,
                        (column.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                        (column.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                        fill=column.cor,
                        tags=column.nome
                    ))

if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


