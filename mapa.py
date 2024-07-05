import elementos as el
import random as rd

class Mapa():
    def __init__(self, tamX, tamY):
        self.tamX = tamX
        self.tamY = tamY

        self.mapa = self.criar_matriz(self.tamX, self.tamY)

    def criar_matriz(self, x, y):
        """
        Cria uma matriz com x*y Quadrados
        """

        return [ [el.Quadrado() for i in range(x)] for i in range(y) ]

    def __str__(self):
        """
        Retorna uma string com o mapa
        """

        ret = ""
        for x in self.mapa:
            for y in x:
                ret += str(y) + " "
            ret += "\n"

        return ret

print(Mapa(5,5))
