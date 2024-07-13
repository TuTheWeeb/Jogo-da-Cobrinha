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
        self.matriz = np.array([ [el.QuadradoVazio([x,y]) for x in range(self.tamX)] for y in range(self.tamY) ])

    def coordenada_random(self) -> list:
        """ Retorna Coordenadas Aleatórias """
        x, y = rd.randint(1, self.tamX-1), rd.randint(1, self.tamY-1)

        if self.checa_se_existe(x, y):
            x, y = self.coordenada_random()

        return [x,y]

    def checa_se_existe(self, x, y):
        """ Retorna True se a coordenada for inválida, False se for válida """
        condicao_quadrado = self.matriz[x][y].nome != "QuadradoVazio"
        condicao_parede = self.matriz[x][y].nome == "Parede"
        condicao_fruta = self.matriz[x][y].nome == "Fruta"
        cobra = self.pegar_cobra()
        condicao_cobra = False

        for c in cobra.corpo:
            if c == [x,y]:
                condicao_cobra = True

        return condicao_quadrado or condicao_cobra or condicao_parede or condicao_fruta

    def gerar_parede(self, quantidade):
        for i in range(quantidade):
            x, y = self.coordenada_random()
            self.matriz[x][y] = el.Parede([x,y])

    def gerar_fruta(self):
        """ Recebe uma coordenada aleatória e gera uma fruta aleatória na coordenada """

        x, y = self.coordenada_random()
        self.matriz[x][y] = el.Fruta([x,y])

    def gerar_cobra(self):
        """ Gera Cobra numa posição fixa apontada para Baixo"""
        x, y = 0, 0
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

    def pegar_cobra(self):
        """
        Retorna uma copia da cobra
        """
        x, y = self.posicao_cobra

        if x < 0 or x >= self.tamX or y < 0 or y >= self.tamY:
            return False

        return self.matriz[self.posicao_cobra[0]][self.posicao_cobra[1]]

    def resetar_atributo_comeu(self):
        x, y = self.posicao_cobra
        self.matriz[x][y].comeu = False

    def resetar_atributo_bateu(self):
        x, y = self.posicao_cobra
        self.matriz[x][y].bateu = False

    def posicao_futura(self):
        x, y = self.posicao_cobra
        x = int(x)
        y = int(y)
        offset_x, offset_y = 0, 0

        if self.direcao == "direita":
            offset_x = 1
        elif self.direcao == "esquerda":
            offset_x = -1
        elif self.direcao == "baixo":
            offset_y = 1
        elif self.direcao == "cima":
            offset_y = -1

        x_futuro = x + offset_x
        y_futuro = y + offset_y


        return [x_futuro, y_futuro]

    def colisao_parede(self, x_futuro, y_futuro):
        x, y = self.posicao_cobra

        if self.matriz[x_futuro][y_futuro].nome == "Parede":
            self.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
            self.matriz[x][y].tamanho -= 1
            self.matriz[x][y].bateu = True

    def colisao_fruta(self, x_futuro, y_futuro):
        x, y = self.posicao_cobra

        if self.matriz[x_futuro][y_futuro].nome == "Fruta":
            self.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
            self.matriz[x][y].tamanho += 1
            self.matriz[x][y].comeu = True

    def colisao_cobra(self, x_futuro, y_futuro):
        cobra = self.pegar_cobra()
        for coordenadas in cobra.corpo:
            if coordenadas == [x_futuro, y_futuro]:
                return True

        return False

    def checar_colisao(self):
        """Checa se a cobra colidiu com o corpo da cobra e retorna True se houver colisão"""
        x_futuro, y_futuro = self.posicao_futura()

        if x_futuro < 0 or x_futuro >= self.tamX or y_futuro < 0 or y_futuro >= self.tamY:
            return False

        self.colisao_fruta(x_futuro, y_futuro)
        self.colisao_parede(x_futuro, y_futuro)
        return self.colisao_cobra(x_futuro, y_futuro)

    def mover_cobra(self):
        """Move a Cobra na Direação dela"""
        x_, y_ = self.posicao_cobra

        if x_ >= self.tamX or y_ >= self.tamY or x_ < 0 or y_ < 0:
            return True

        colisao = self.checar_colisao() or self.matriz[x_][y_].tamanho == 0

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
        if x >= self.tamX or y >= self.tamY or x < 0 or y < 0:
            return True

        # atualiza as coordenadas da cobra em sua classe
        self.matriz[x_][y_].coordenadas = [x, y]

        # Atualiza as coordenadas da cobra no mapa
        self.matriz[x][y] = self.matriz[x_][y_]
        self.matriz[x_][y_] = el.QuadradoVazio([x_,y_])

        return colisao

    def atualizar_mapa(self):
        """Checa todos os quadrados de corpo da cobra e atualiza o timer """
        for x in range(self.tamX):
            for y in range(self.tamY):
                if self.matriz[x][y] != "QuadradoVazio": continue
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

