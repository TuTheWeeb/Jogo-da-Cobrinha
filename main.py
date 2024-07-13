from constantes import *
import elementos as el
from mapa import Mapa
import numpy as np
#from random import choice
#import integracao as integ
from tkinter import *
from PIL import ImageTk, Image

class App():
    def __init__(self, master=None):
        """
        Define as caracteristicas da Applicação

        Keywords:
        Config -- 
        Resizable -- Desabilita a alteraçao de tamanho da janela
        Geometria -- Tamanho da Janela
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
        
        #Cria imagem de fundo 
        menu_canvas = Canvas(self.Menu, width=GAME_WIDTH, height=GAME_HEIGHT)
        menu_canvas.background_image = background_image
        menu_canvas.create_image(0, 0, anchor=NW, image=background_image)
        menu_canvas.place(x=0,y=0)
        
        #Cria titulo
        self.nome = Label(self.Menu, text="Jogo da Cobrinha!", font=fonte)
        self.nome.place(x=(GAME_WIDTH//2 - 90), y=10)

        #Cria botoes
        y_botao = 0.6
        
        self.botao_inciar = Button(self.Menu, text="Jogar", font=fonte, height=2, width=10, command=self.jogar)
        self.botao_inciar.place(relx=0.3, rely=y_botao, anchor=CENTER)

        self.botao_sair = Button(self.Menu, text="Sair", font=fonte, height=2, width=10, command=self.master.destroy)
        self.botao_sair.place(relx=0.7, rely=y_botao, anchor=CENTER)

    def jogar(self):
        """
        Cria Funcionalidades do Jogo
        """
        self.Jogo.tkraise()
        self.score = 0

        #Placar de pontuação
        self.Placar = Label(self.Jogo, text="Score: {}".format(self.score), font=("consolas", 40))
        self.Placar.pack()

        #Criação da canvas 
        self.canvas = Canvas(self.Jogo, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()
        self.fator_de_correcao = (GAME_WIDTH - MAPA_WIDTH)/2
        self.grid = self.canvas.create_rectangle(self.fator_de_correcao, 0,
                                                 MAPA_WIDTH + self.fator_de_correcao, MAPA_HEIGHT,
                                                 fill='', width=10)

        # Controles
        self.master.bind('<Left>', lambda event: self.Mapa.mudar_direcao("esquerda"))
        self.master.bind('<Right>', lambda event: self.Mapa.mudar_direcao("direita"))
        self.master.bind('<Down>', lambda event: self.Mapa.mudar_direcao("baixo"))
        self.master.bind('<Up>', lambda event: self.Mapa.mudar_direcao("cima"))
        self.master.bind('<Escape>', lambda event: self.master.quit())

        self.lista_elementos = []
        self.Mapa = Mapa()
        self.Mapa.gerar_cobra()
        self.Mapa.gerar_parede(2)
        self.Mapa.gerar_fruta()
        self.after_id = []

        self.renderizar()

    def addicionar_obj(self, obj): #O que essa função faz??
        self.lista_elementos.append(obj)

    def limpar_elementos(self):
        for item in self.lista_elementos:
            self.canvas.delete(item)

        self.lista_elementos = []

    def diminuir_cobra(self):
        cobra_ou_nao = self.Mapa.pegar_cobra()
        x, y = cobra_ou_nao.coordenadas

        self.canvas.delete(cobra_ou_nao.corpo_render[-1])
        self.canvas.delete(cobra_ou_nao.corpo[-1])
        self.Mapa.matriz[x][y].corpo.pop()
        self.Mapa.matriz[x][y].corpo_render.pop()

    def renderizar(self):
        # Condiciona que se na proxima posição for invalida então game over my boy
        if self.Mapa.mover_cobra():
            self.GameOver.tkraise()
            self.game_over()

        for linha in self.Mapa.matriz:
            for objeto in linha:
                if objeto.nome == "QuadradoVazio": continue

                cobra_ou_nao = self.Mapa.pegar_cobra()
                if cobra_ou_nao == False: continue

                if cobra_ou_nao.comeu == True:
                    self.limpar_elementos()
                    self.Mapa.gerar_fruta()
                    self.Mapa.gerar_parede(1)

                    global VELOCIDADE
                    VELOCIDADE -= 5

                    self.score += 1
                    self.Placar.config(text="Score: {}".format(self.score))

                    self.Mapa.resetar_atributo_comeu()

                if cobra_ou_nao.bateu == True:
                    self.limpar_elementos()
                    self.Mapa.gerar_parede(2)

                    VELOCIDADE -= 10

                    self.score -= 1
                    self.Placar.config(text="Score: {}".format(self.score))
                    self.diminuir_cobra()

                    self.Mapa.resetar_atributo_bateu()

                if objeto.nome == "Cobra":
                    x, y = self.Mapa.posicao_cobra

                    if len(self.Mapa.matriz[x][y].corpo_render) == self.Mapa.matriz[x][y].tamanho:
                        self.canvas.delete(cobra_ou_nao.corpo_render[-1])
                        self.canvas.delete(cobra_ou_nao.corpo[-1])
                        del self.Mapa.matriz[x][y].corpo_render[-1]
                        del self.Mapa.matriz[x][y].corpo[-1]

                    corpo = self.canvas.create_rectangle(
                            self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                            objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                            self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                            (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                            fill=objeto.cor,
                            tags=objeto.nome
                        )

                    self.Mapa.matriz[x][y].corpo_render.insert(0, corpo)
                    self.Mapa.matriz[x][y].corpo.insert(0, ([(self.canvas.coords(corpo)[0] - self.fator_de_correcao)//WIDTH_PROPORTIONS, self.canvas.coords(corpo)[1]//HEIGHT_PROPORTIONS]))

                elif objeto.nome == "Fruta":
                    fruta = self.canvas.create_rectangle(
                                self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                                objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                                self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                                (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                                fill=objeto.cor,
                                tags=objeto.nome
                            )
                    self.addicionar_obj(fruta)
                elif objeto.nome == "Parede":
                    parede = self.canvas.create_rectangle(
                                self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                                objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                                self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                                (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                                fill=objeto.cor,
                                tags=objeto.nome
                            )
                    self.addicionar_obj(parede)

        self.Mapa.atualizar_mapa()
        self.proximo_frame()

    def proximo_frame(self):
        self.after_id.append(self.master.after(VELOCIDADE, self.renderizar))
        #self.after_id.append(self.master.after(250, self.renderizar))

    def game_over(self):
        for ide in self.after_id:
            self.master.after_cancel(ide)

        for item in self.lista_elementos:
            self.canvas.delete(item)

        self.GameOver_msg = Label(self.GameOver, text="Game Over \n Pressione Esc para sair", font=("consolas", 40))
        self.GameOver_msg.place(relx=0.5, rely=0.3, anchor=CENTER)


if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


