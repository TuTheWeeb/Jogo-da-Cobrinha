#Módulo para descrever os diferentes tipos de objetos que podem aparecer na canvas
from constantes import *
import numpy as np

class QuadradoVazio():   
    def __init__(self): 
        self.nome = "Fundo"
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
        self.coordenadas = coordenadas

    def __str__(self):
        return self.nome
    
class Apple(Fruta):
    def __init__super():
        def __init__(self):
            self.nome = "Maçã"
            self.cor = APPLE_COLOR
            self.pontos = 100

class Laranja(Fruta):
    def __init__super():
        def __init__(self):
            self.nome = "Laranja"
            self.cor = ORANGE_COLOR
            self.pontos = 450

class Limao(Fruta):
    def __init__super():
        def __init__(self):
            self.nome = "Limão"
            self.cor = LEMON_COLOR
            self.pontos = 55
