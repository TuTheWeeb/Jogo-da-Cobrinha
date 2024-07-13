from constantes import *
import random as rd

"""Módulo para descrever os diferentes tipos de objetos que podem aparecer na canvas"""

class QuadradoVazio():   
    def __init__(self, coordenadas: list): 
        """ Cria Classe para Background """
        self.nome = "QuadradoVazio"
        self.coordenadas = coordenadas
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
        self.cor = cor
        self.coordenadas = [0,0]
        self.corpo = [self.coordenadas]
        self.corpo_render = []
        self.tamanho = 3
        self.comeu = False
        self.bateu = False

    def __str__(self):
        return self.nome


class Parede(QuadradoVazio):
    def __init__(self, coordenadas: list):
        """
        Cria Objeto para as Paredes

        Keyword Arguments:
        Coordenadas -- Coordenadas onde vao gerar paredes no começo do jogo
        Tamanho -- Tamanho das paredes Geradas 
        """

        self.nome = "Parede"
        self.cor = WALL_COLOR
        self.coordenadas = coordenadas

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
        self.timer = 100
        
    def __str__(self):
        return self.nome
