import elementos as el
import random as rd
from constantes import *
import numpy as np


class Mapa():
    def __init__(self, tamX = PIXEL_CONTROL, tamY = PIXEL_CONTROL):
        """ Cria um Objeto da Classe Mapa """
        self.tamX = tamX
        self.tamY = tamY
        self.criar_matriz()


    def criar_matriz(self):
        """
        Cria um array para o Mapa preenchido com QuadradoVazio

        tamX -- Tamanho do Eixo X (Default = PIXEL_CONTROL+1)
        tamY -- Tamanho do Eixo Y (Default = PIXEL_CONTROL+1)
        """
        self.matriz = np.array([ [el.QuadradoVazio() for x in range(self.tamX)] for y in range(self.tamY) ])

    def coordenada_random(self) -> list:
        """ Retorna Coordenadas Aleatórias """
        x, y = rd.randint(1, self.tamX-1), rd.randint(1, self.tamY-1)

        if self.checa_se_existe(x, y):
            x, y = self.coordenada_random()

        return [x,y]

    def checa_se_existe(self, x, y):
        """ Retorna True se a coordenada for inválida, False se for válida """
        return self.matriz[x][y].nome != "QuadradoVazio"

    def gerar_fruta(self):
        """ Recebe uma coordenada aleatória e gera uma fruta aleatória na coordenada """

        x, y = self.coordenada_random()
        self.matriz[x][y] = el.Fruta([x,y])

    def gerar_cobra(self):
        """ Gera Cobra numa posição fixa apontada para Baixo"""
        x, y = 2, 2
        self.posicao_cobra = [x, y]
        self.direcao = "baixo"
        cobra = el.Cobra("#109f09")
        cobra.coordenadas = [x, y]
        self.matriz[x][y] = cobra

    def mudar_direcao(self, nova_direcao):
        """Muda a var direção que será depois atribuída à cobras"""

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

    def mover_cobra(self):
        """Move a Cobra na Direação dela"""
        x_, y_ = self.posicao_cobra

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
        if x >= self.tamX - 1 or y >= self.tamY - 1 or x < 0 or y < 0:
            return True

        # atualiza as coordenadas da cobra em sua classe
        self.matriz[x_][y_].coordenadas = [x, y]

        # Atualiza as coordenadas da cobra no mapa
        self.matriz[x][y] = self.matriz[x_][y_]
        self.matriz[x_][y_] = el.QuadradoRenderizado([x_,y_])

        return False

    def atualizar_mapa(self):
        """Checa todos os quadrados de corpo da cobra e atualiza o timer """
        for x in range(self.tamX):
            for y in range(self.tamY):
                if self.matriz[x][y] != el.QuadradoVazio() or self.matriz[x][y] != el.QuadradoRenderizado : continue
                self.matriz[x][y].timer -= 1

    def __str__(self):
        """ Retorna String contendo os valores do Array """

        #Sobrecarga de print para testes
        ret = ""
        for x in self.matriz:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

