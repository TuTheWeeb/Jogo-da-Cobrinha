#Módulo para descrever os diferentes tipos de objetos que podem aparecer na canvas
from constantes import *
import numpy as np
import random as rd

class QuadradoVazio():   
    def __init__(self): 
        self.nome = "QuadradoVazio"
        self.cor = BACKGROUND_COLOR

    def __str__(self):
        return self.nome
    
#Elementos que podem spawnar no mapa
class Cobra(QuadradoVazio):
    def __init__(self, cor):
        self.nome = "Cobra"
        self.partes = 3
        self.cor = cor
        self.coordenadas = []
        


    def __str__(self):
        return self.nome

class Parede(QuadradoVazio):
    def __init__(self, coordenadas, tamanho: int):
        self.nome = "Parede"
        self.cor = WALL_COLOR
        self.coordenadas = coordenadas
        self.tamanho = tamanho

    def __str__(self):
        return self.nome

#FRUTAS            
class Fruta(QuadradoVazio):
    def __init__(self, coordenadas: list):
        self.nome = "Fruta"
        self.coordenadas = coordenadas
        self.pontos = rd.randint(1, 100)
        self.cor = rd.choice([APPLE_COLOR, ORANGE_COLOR, LEMON_COLOR])
    def __str__(self):
        return self.nome
