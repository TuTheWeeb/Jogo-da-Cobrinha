import elementos as el
import random as rd
from constantes import *
import numpy as np


class Mapa():
    def __init__(self, tamX = 11, tamY = 11):
        """ Cria um Objeto da Classe Mapa """
        self.tamX = tamX
        self.tamY = tamY
        self.criar_matriz()


    def criar_matriz(self):
        """
        Cria um array para o Mapa preenchido com QuadradoVazio

        tamX -- Tamanho do Eixo X (Default = 11)
        tamY -- Tamanho do Eixo Y (Default = 11)
        """
        self.matriz = np.array([ [el.QuadradoVazio() for x in range(self.tamX)] for y in range(self.tamY) ])

    def coordenada_random(self) -> list:
        """ Retorna Coordenadas Aleatórias """
        x, y = rd.randint(0, self.tamX-1), rd.randint(0, self.tamY-1)

        if self.checa_se_existe(x, y):
            x, y = self.coordenada_random()

        return [x,y]

    def checa_se_existe(self, x, y):
        """ Retorna True se a coordenada for válida, False se não for válida """
        return self.matriz[x][y].nome != "QuadradoVazio"

    def gerar_fruta(self):
        """ Recebe uma coordenada aleatória e gera uma fruta aleatória na coordenada """

        x, y = self.coordenada_random()
        self.matriz[x][y] = el.Fruta([x,y])

    def gerar_cobra(self):
        """ Gera Cobra numa posição aleatoria apontada para a Direita"""
        x, y = self.coordenada_random()
        self.posicao_cobra = [x, y]
        self.direcao = "direita"

        self.matriz[x][y] = el.Cobra("#FFFFFF")

    def mudar_direcao(self, direcao):
        """Muda a direção da cobra"""
        self.direcao = direcao

    def mover_cobra(self):
        """Move a Cobra na Direação dela"""
        x_, y_ = self.posicao_cobra

        if self.fora_da_matriz():
            return True

        if self.direcao == "direita":
            self.posicao_cobra[0] += 1
        elif self.direcao == "esquerda":
            self.posicao_cobra[0] -= 1
        elif self.direcao == "baixo":
            self.posicao_cobra[1] += 1
        elif self.direcao == "cima":
            self.posicao_cobra[1] -= 1

        x, y = self.posicao_cobra

        self.matriz[x][y] = self.matriz[x_][y_]
        self.matriz[x_][y_] = el.QuadradoVazio()

        return False

    def proxima_posicao(self):
        posicao_cobra = self.posicao_cobra

        if self.direcao == "direita":
            posicao_cobra[0] += 1
        elif self.direcao == "esquerda":
            posicao_cobra[0] -= 1
        elif self.direcao == "baixo":
            posicao_cobra[1] += 1
        elif self.direcao == "cima":
            posicao_cobra[1] -= 1

        return posicao_cobra

    def fora_da_matriz(self):
        x, y = self.proxima_posicao()
        if x >= self.tamX or y >= self.tamY or x < 0 or y < 0:
            return True

    def __str__(self):
        """ Retorna String contendo os valores do Array """

        #Sobrecarga de print para testes
        ret = ""
        for x in self.matriz:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

