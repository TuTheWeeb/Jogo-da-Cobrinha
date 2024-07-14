from constantes import *
from mapa import Mapa
import random as rd
import integracao as integ
from tkinter import *
from PIL import ImageTk, Image
#from playsound import playsound

class App():
    def __init__(self, master=None):
        """
        Define as caracteristicas da Applicação

        Keywords:
        Config -- 
        Resizable -- Desabilita a alteração de tamanho da janela
        Geometry -- Tamanho da Janela
        """
        # Definições
        self.master = master
        self.master.config(height=GAME_HEIGHT, width=GAME_WIDTH)
        self.master.resizable(False, False)
        self.master.title("Jogo da Cobrinha")
        self.master.geometry(f"{GAME_WIDTH}x{GAME_HEIGHT}")


        # Cria as paginas ou Frames
        self.Menu = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.Seletor_Dificuldade = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.Jogo = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.GameOver = Frame(self.master, height=GAME_HEIGHT, width=GAME_WIDTH)

        # Coloca as paginas em modelo grid
        self.Menu.grid(row=0, column=0, sticky="nsew")
        self.Seletor_Dificuldade.grid(row=0, column=0, sticky="nsew")
        self.Jogo.grid(row=0, column=0, sticky="nsew")
        self.GameOver.grid(row=0, column=0, sticky="nsew")
        self.menu()

    def menu(self):
        """Cria a janela do menu inicial"""

        background_image = Image.open('Cobra.jpg')
        background_image = background_image.resize((GAME_WIDTH, GAME_HEIGHT))
        background_image = ImageTk.PhotoImage(background_image)

        self.fonte=("Comic Sans", 15)

        self.Menu.tkraise()
        
        #Cria imagem de fundo 
        self.menu_canvas = Canvas(self.Menu, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.menu_canvas.background_image = background_image
        self.menu_canvas.create_image(0, 0, anchor=NW, image=background_image)
        self.menu_canvas.place(x=0,y=0)
        
        #Cria titulo
        self.nome = Label(self.Menu, text="Jogo da Cobrinha!", font=self.fonte)
        self.nome.place(x=(GAME_WIDTH//2 - 90), y=10)

        #Cria botoes
        y_botao = 0.6
        
        self.botao_inciar = Button(self.Menu, text="Jogar", font=self.fonte, height=2, width=10, command=self.dificuldade)
        self.botao_inciar.place(relx=0.3, rely=y_botao, anchor=CENTER)

        self.botao_sair = Button(self.Menu, text="Sair", font=self.fonte, height=2, width=10, command=self.master.destroy)
        self.botao_sair.place(relx=0.7, rely=y_botao, anchor=CENTER)

    def dificuldade(self):
        self.botao_inciar.place_forget()
        self.botao_sair.place_forget()

        self.Facil = Button(self.Menu, text="Facil", font=self.fonte, height=2, width=10, command=self.facil)
        self.Facil.place(relx=0.1, rely=0.5, anchor=CENTER)

        self.Medio = Button(self.Menu, text="medio", font=self.fonte, height=2, width=10, command=self.medio)
        self.Medio.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.Dificil = Button(self.Menu, text="dificil", font=self.fonte, height=2, width=10, command=self.dificil)
        self.Dificil.place(relx=0.9, rely=0.5, anchor=CENTER)

    def facil(self):
        """
        Seletor de dificuldade facil
        """
        global VELOCIDADE
        VELOCIDADE = 350
        self.jogar()

    def medio(self):
        "Seletor de dificuldade media"
        global VELOCIDADE
        VELOCIDADE = 250
        self.jogar()

    def dificil(self):
        """
        Seletor de dificuldade dificil
        """
        global VELOCIDADE
        VELOCIDADE = 150
        self.jogar()

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
        self.master.bind('<Left>', lambda event: self.mapa.mudar_direcao("esquerda"))
        self.master.bind('<Right>', lambda event: self.mapa.mudar_direcao("direita"))
        self.master.bind('<Down>', lambda event: self.mapa.mudar_direcao("baixo"))
        self.master.bind('<Up>', lambda event: self.mapa.mudar_direcao("cima"))
        self.master.bind('<Escape>', lambda event: self.master.quit())

        self.buffer_renderizacao = []
        self.mapa = Mapa()
        self.mapa.gerar_cobra()
        self.mapa.gerar_parede(2)
        self.mapa.gerar_fruta()
        self.after_id = []

        self.renderizar()

    def adicionar_objeto(self, obj):
        """
        Adiciona um objeto ao buffer de renderização
        """
        self.buffer_renderizacao.append(obj)

    def limpar_buffer(self):
        """
        Limpa o buffer de renderização.
        """
        for item in self.buffer_renderizacao:
            self.canvas.delete(item)

        self.buffer_renderizacao = []

    def diminuir_cobra(self):
        """
        Diminui o tamanho da cobra
        """
        cobra_ou_nao = self.mapa.pegar_cobra()
        x, y = cobra_ou_nao.coordenadas

        self.canvas.delete(cobra_ou_nao.corpo_render[-1])
        self.mapa.matriz[x][y].corpo.pop()
        self.mapa.matriz[x][y].corpo_render.pop()

    def renderizar(self):
        # Condiciona que se na proxima posição for invalida então game over my boy
        if self.mapa.mover_cobra():
            self.GameOver.tkraise()
            self.game_over()

        for linha in self.mapa.matriz:
            for objeto in linha:
                if objeto.nome == "QuadradoVazio": continue

                cobra_ou_nao = self.mapa.pegar_cobra()
                if cobra_ou_nao == False: continue

                if cobra_ou_nao.comeu == True:
                    self.limpar_buffer()
                    self.mapa.gerar_fruta()

                    if rd.random() > 0.5:
                        self.mapa.gerar_parede(1)

                    global VELOCIDADE
                    if VELOCIDADE > 70:
                        VELOCIDADE -= 5

                    self.score += 1
                    self.Placar.config(text="Score: {}".format(self.score))

                    integ.resetar_atributo_comeu(self.mapa)

                if cobra_ou_nao.bateu == True:
                    self.limpar_buffer()
                    self.mapa.gerar_parede(2)

                    if VELOCIDADE > 70:
                        VELOCIDADE -= 10

                    self.score -= 1
                    self.Placar.config(text="Score: {}".format(self.score))
                    self.diminuir_cobra()

                    integ.resetar_atributo_bateu(self.mapa)

                if objeto.nome == "Cobra":
                    x, y = self.mapa.posicao_cobra

                    tamanho = len(self.mapa.matriz[x][y].corpo_render)

                    if tamanho == self.mapa.matriz[x][y].tamanho and tamanho > 0:
                        self.canvas.delete(cobra_ou_nao.corpo_render[-1])
                        del self.mapa.matriz[x][y].corpo_render[-1]
                        del self.mapa.matriz[x][y].corpo[-1]

                    corpo = self.canvas.create_rectangle(
                            self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                            objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                            self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                            (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                            fill=objeto.cor,
                            tags=objeto.nome
                        )

                    coordenadas = self.canvas.coords(corpo)
                    coordenadas = (coordenadas[0] - self.fator_de_correcao, coordenadas[1])
                    self.mapa.atualizar_cobra(coordenadas, corpo)

                elif objeto.nome == "Fruta":
                    fruta = self.canvas.create_rectangle(
                                self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                                objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                                self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                                (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                                fill=objeto.cor,
                                tags=objeto.nome
                            )
                    self.adicionar_objeto(fruta)
                elif objeto.nome == "Parede":
                    parede = self.canvas.create_rectangle(
                                self.fator_de_correcao + objeto.coordenadas[0]*WIDTH_PROPORTIONS,
                                objeto.coordenadas[1]*HEIGHT_PROPORTIONS,
                                self.fator_de_correcao + (objeto.coordenadas[0]*WIDTH_PROPORTIONS)+WIDTH_PROPORTIONS,
                                (objeto.coordenadas[1]*HEIGHT_PROPORTIONS)+HEIGHT_PROPORTIONS,
                                fill=objeto.cor,
                                tags=objeto.nome
                            )
                    self.adicionar_objeto(parede)

        self.proximo_frame()

    def proximo_frame(self):
        """Chama o próximo frame do jogo"""
        self.after_id.append(self.master.after(VELOCIDADE, self.renderizar))

    def game_over(self):
        """Constrói a janela GameOver"""
        for ide in self.after_id:
            self.master.after_cancel(ide)

        for item in self.buffer_renderizacao:
            self.canvas.delete(item)

        self.GameOver_msg = Label(self.GameOver, text="Game Over \n Pressione Esc para sair", font=("consolas", 40))
        self.GameOver_msg.place(relx=0.5, rely=0.3, anchor=CENTER)


if __name__ == "__main__":
    master = Tk()
    app = App(master)
    mainloop()


