#Módulo para descrever os diferentes tipos de objetos que podem aparecer na canvas
from constantes import *
import numpy as np
import random as rd

class QuadradoVazio():   
    def __init__(self): 
        """ Cria Classe para Background """
        self.nome = "QuadradoVazio"
        self.cor = BACKGROUND_COLOR

    def __str__(self):
        return self.nome

#Elementos que podem spawnar no mapa
class Corpo_Cobra(QuadradoVazio):
    def __init__(self, timer):
        self.timer = timer

    def tempo(self):
        self.timer -= 1


class Cobra(QuadradoVazio):
    def __init__(self, cor):
        """ 
        Cria Objeto para a Cobra

        Keyword Arguments:
        Partes -- Tamanho da Cobra ao Iniciar o Jogo
        Coordenadas -- Lista de Coordenadas para as partes da cobra
        """
        self.nome = "Cobra"
        self.partes = 3
        self.cor = cor
        self.coordenadas = [0,0]

    def __str__(self):
        return self.nome

    def criar_corpo(self):
        pass

class Parede(QuadradoVazio):
    def __init__(self, coordenadas, tamanho: int):
        """
        Cria Objeto para as Paredes

        Keyword Arguments:
        Coordenadas -- Coordenadas onde vao gerar paredes no começo do jogo
        Tamanho -- Tamanho das paredes Geradas 
        """
        self.nome = "Parede"
        self.cor = WALL_COLOR
        self.coordenadas = coordenadas
        self.tamanho = tamanho

    def __str__(self):
        return self.nome

#FRUTAS            
class Fruta(QuadradoVazio):
    def __init__(self, coordenadas: list):
        """
        Cria Objeto para as Frutas

        Keyword Arguments:
        Coordenadas -- Cordenadas onde vai ser gerada a Fruta
        Pontos -- Pontos que a Fruta vale
        Cor -- Qual fruta vai ser gerada
        """
        self.nome = "Fruta"
        self.coordenadas = coordenadas
        self.pontos = rd.randint(1, 100)
        self.cor = rd.choice([APPLE_COLOR, ORANGE_COLOR, LEMON_COLOR])
    def __str__(self):
        return self.nome
