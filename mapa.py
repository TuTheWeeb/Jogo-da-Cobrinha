import elementos as el
import random as rd
from constantes import *
import numpy as np


class Mapa():
    def __init__(self, tamX = 11, tamY = 11):
        self.tamX = tamX
        self.tamY = tamY
        self.criar_matriz()


    def criar_matriz(self):
        """
        Cria um array de tamX*tamY Quadrados
        """
        self.matriz = np.array([ [el.QuadradoVazio() for x in range(self.tamX)] for y in range(self.tamY) ])

    def coordenada_random(self) -> list:
        """ Gera uma coordenada aleatória dentro das dimensões do 
            do mapa.
        """
        x, y = rd.randint(0, self.tamX-1), rd.randint(0, self.tamY-1)

        if self.checa_se_existe(x, y):
            x, y = self.coordenada_random()

        return [x,y]

    def checa_se_existe(self, x, y):
        return self.matriz[x][y].nome != "QuadradoVazio"

    def gerar_fruta(self):
        x, y = self.coordenada_random()
        self.matriz[x][y] = el.Fruta([x,y])

    def __str__(self):
        """
        Sobrecarga de print para testes,
        retorna uma string com o mapa. 
        """
        ret = ""
        for x in self.matriz:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

