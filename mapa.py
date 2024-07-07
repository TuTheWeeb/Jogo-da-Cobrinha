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
        Cria um array para o Mapa

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

    def __str__(self):
        """ Retorna String contendo os valores do Array """
        
        #Sobrecarga de print para testes
        ret = ""
        for x in self.matriz:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

