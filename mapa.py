import elementos as el
import random as rd
from constantes import *
import numpy as np


class Mapa():
    def __init__(self, tamX = GAME_WIDTH, tamY = GAME_HEIGHT, pixel_size = PIXEL_SIZE): 
        self.tamX = tamX
        self.tamY = tamY
        self.mapa = self.criar_matriz(self.tamX, self.tamY)
        self.pixel_size = pixel_size


    def criar_matriz(self):
        """
        Cria um array de x*y Quadrados
        """
        #[ [el.QuadradoVazio() for i in range(self.tamX)] for i in range(self.tamY) ]
        return np.empty(self.tamX, self.tamY)
    
    
    def coordenada_random(self)-> list:
        """ Gera uma coordenada aleatória dentro das dimensões do 
            do mapa.
        """
        x = rd.randint(0, WIDTH_PROPORTIONS) * PIXEL_SIZE
        y = rd.randint(0, HEIGHT_PROPORTIONS) * PIXEL_SIZE

        return [x,y]

    def __str__(self):   
        """
        Sobrecarga de print para testes,
        retorna uma string com o mapa. 
        """
        ret = ""
        for x in self.mapa:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

