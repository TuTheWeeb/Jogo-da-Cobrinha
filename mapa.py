import elementos as el
import random as rd
from constantes import *
import numpy as np
import integracao as integ

class Mapa():
    def __init__(self, tamX = PIXEL_CONTROL, tamY = PIXEL_CONTROL):
        """ Cria um Objeto da Classe Mapa """
        self.tamX = tamX
        self.tamY = tamY
        self.criar_matriz()


    def criar_matriz(self):
        """
        Cria um array para o Mapa preenchido com QuadradoVazio

        tamX -- Tamanho do Eixo X (Default = PIXEL_CONTROL)
        tamY -- Tamanho do Eixo Y (Default = PIXEL_CONTROL)
        """
        self.matriz = np.array([ [el.QuadradoVazio([x,y]) for x in range(self.tamX)] for y in range(self.tamY) ])

    def coordenada_random(self) -> list:
        """ Retorna Coordenadas Aleatórias """
        x, y = rd.randint(1, self.tamX-1), rd.randint(1, self.tamY-1)

        if self.checa_se_existe(x, y):
            x, y = self.coordenada_random()

        return [x,y]

    def checa_se_existe(self, x, y) -> bool:
        """ Retorna True se a coordenada for inválida, False se for válida """
        condicao_quadrado = self.matriz[x][y].nome != "QuadradoVazio"
        condicao_parede = self.matriz[x][y].nome == "Parede"
        condicao_fruta = self.matriz[x][y].nome == "Fruta"
        cobra = self.pegar_cobra()
        condicao_cobra = False

        coordenadas = set(cobra.corpo)
        if (x,y) in coordenadas:
            condicao_cobra = True

        return condicao_quadrado or condicao_cobra or condicao_parede or condicao_fruta


    def gerar_parede(self, quantidade: int):
        """ Gera uma quantidade pré-determinada de paredes em uma coordenada aleatória """
        for i in range(quantidade):
            x, y = self.coordenada_random()
            self.matriz[x][y] = el.Parede([x,y])

    def gerar_fruta(self):
        """ Gera uma fruta em uma coordenada aleatória """
        x, y = self.coordenada_random()
        self.matriz[x][y] = el.Fruta([x,y])


    def gerar_cobra(self):
        """ Gera Cobra numa posição fixa apontada para Baixo"""
        x, y = 0, 0
        self.posicao_cobra = [x, y]
        self.direcao = "baixo"
        cobra = el.Cobra("#109f09")
        cobra.coordenadas = [x, y]
        self.matriz[x][y] = cobra


    def pegar_cobra(self):
        """
        Retorna uma copia da cobra
        """
        x, y = self.posicao_cobra

        if x < 0 or x >= self.tamX or y < 0 or y >= self.tamY:
            return False

        return self.matriz[x][y]


    def mudar_direcao(self, nova_direcao):
        """Muda a var direção que será depois atribuída à Cobra e seu Corpo"""

        if self.direcao == "direita":
            if nova_direcao != "esquerda":
                self.direcao = nova_direcao
        elif self.direcao == "esquerda":
            if nova_direcao != "direita":
                self.direcao = nova_direcao
        elif self.direcao == "cima":
            if nova_direcao != "baixo":
                self.direcao = nova_direcao
        elif self.direcao == "baixo":
            if nova_direcao != "cima":
                self.direcao = nova_direcao


    def posicao_futura(self)-> list:
        """Retorna as coordenadas da próxima posição em que a cobra vai estar
        baseado na direção atual."""
        x, y = self.posicao_cobra
        x = int(x)
        y = int(y)
        offset_x, offset_y = 0, 0

        if self.direcao == "direita":
            offset_x = 1
        elif self.direcao == "esquerda":
            offset_x = -1
        elif self.direcao == "baixo":
            offset_y = 1
        elif self.direcao == "cima":
            offset_y = -1

        x_futuro = x + offset_x
        y_futuro = y + offset_y

        return [x_futuro, y_futuro]

    def checar_colisao(self)-> bool:
        """ Checa se a cobra colidiu com algo. Colisões com Fruta ou Parede
        geram eventos, colisão com o corpo da cobra retorna True. """
        x_futuro, y_futuro = self.posicao_futura()

        if x_futuro < 0 or x_futuro >= self.tamX or y_futuro < 0 or y_futuro >= self.tamY:
            return False

        integ.colisao_fruta(self, x_futuro, y_futuro)
        integ.colisao_parede(self, x_futuro, y_futuro)

        return integ.colisao_cobra(self, x_futuro, y_futuro)


    def mover_cobra(self)-> bool:
        """Move a Cobra na Direação dela. retorna True se houver colisão fatal."""
        x_, y_ = self.posicao_cobra

        if x_ >= self.tamX or y_ >= self.tamY or x_ < 0 or y_ < 0:
            return True

        colisao = self.checar_colisao() or self.matriz[x_][y_].tamanho == 0

        if self.direcao == "direita":
            self.posicao_cobra[0] += 1
        elif self.direcao == "esquerda":
            self.posicao_cobra[0] -= 1
        elif self.direcao == "baixo":
            self.posicao_cobra[1] += 1
        elif self.direcao == "cima":
            self.posicao_cobra[1] -= 1

        x, y = self.posicao_cobra

        # Checa se a cobra esta fora do mapa
        if x >= self.tamX or y >= self.tamY or x < 0 or y < 0:
            return True

        # atualiza as coordenadas da cobra em sua classe
        self.matriz[x_][y_].coordenadas = (x, y)

        # Atualiza as coordenadas da cobra no mapa
        self.matriz[x][y] = self.matriz[x_][y_]
        self.matriz[x_][y_] = el.QuadradoVazio([x_,y_])

        return colisao


    def atualizar_cobra(self, coordenadas: list, corpo):
        """
        Atualiza a o corpo da cobra
        """
        x, y = self.posicao_cobra
        self.matriz[x][y].corpo_render.insert(0, corpo)
        self.matriz[x][y].corpo.insert(0, (( coordenadas[0]//WIDTH_PROPORTIONS, coordenadas[1]//HEIGHT_PROPORTIONS )))

    def __str__(self):
        """ Retorna String contendo os valores do Array """

        #Sobrecarga de print para testes
        ret = ""
        for x in self.matriz:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

