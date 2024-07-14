import elementos as el
import mapa as mp

"""Funções que atualizam atributos dos objetos presentes no módulo elementos.py"""

def resetar_atributo_comeu(mapa):
    """Reseta o atribudo Cobra.comeu para False"""
    x, y = mapa.posicao_cobra
    mapa.matriz[x][y].comeu = False


def resetar_atributo_bateu(mapa):
    """Reseta o atribudo Cobra.bateu para False"""
    x, y = mapa.posicao_cobra
    mapa.matriz[x][y].bateu = False

def colisao_parede(mapa, x_futuro, y_futuro):
    """
    Detecta colisao da cobra com uma parede
    """
    x, y = mapa.posicao_cobra

    if mapa.matriz[x_futuro][y_futuro].nome == "Parede":
        mapa.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
        mapa.matriz[x][y].tamanho -= 1
        mapa.matriz[x][y].bateu = True

def colisao_cobra(mapa, x_futuro, y_futuro):
    """
    Detecta colisao da cobra com o seu proprio corpo, utiliza um set porque a pesquisa é muito mais rápida.
    """
    coordenadas = set(mapa.pegar_cobra().corpo)
    if (x_futuro, y_futuro) in coordenadas:
        return True

    return False

def colisao_fruta(mapa, x_futuro, y_futuro):
    """
    Detecta colisao da cobra com uma fruta
    """
    x, y = mapa.posicao_cobra

    if mapa.matriz[x_futuro][y_futuro].nome == "Fruta":
        mapa.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
        mapa.matriz[x][y].tamanho += 1
        mapa.matriz[x][y].comeu = True

    return mapa.matriz



