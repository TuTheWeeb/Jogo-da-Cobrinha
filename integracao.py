import elementos as el
import mapa as mp 

"""Funções que atualizam atributos dos objetos presentes no módulo elementos.py"""

def resetar_atributo_comeu(mapa: mp.Mapa):
    """Reseta o atribudo Cobra.comeu para False"""
    x, y = mapa.posicao_cobra
    mapa.matriz[x][y].comeu = False


def resetar_atributo_bateu(mapa: mp.Mapa):
    """Reseta o atribudo Cobra.bateu para False"""
    x, y = mapa.posicao_cobra
    mapa.matriz[x][y].bateu = False


def atualizar_timer(mapa: mp.Mapa):
        """Checa todos os quadrados de corpo da cobra e atualiza o timer """
        for x in range(mapa.tamX):
            for y in range(mapa.tamY):
                if mapa.matriz[x][y] != "QuadradoVazio": continue
                mapa.matriz[x][y].timer -= 1


def colisao_parede(mapa: mp.Mapa, x_futuro, y_futuro):
    x, y = mapa.posicao_cobra

    if mapa.matriz[x_futuro][y_futuro].nome == "Parede":
        mapa.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
        mapa.matriz[x][y].tamanho -= 1
        mapa.matriz[x][y].bateu = True


def colisao_fruta(mapa: mp.Mapa, x_futuro, y_futuro):
    x, y = mapa.posicao_cobra

    if mapa.matriz[x_futuro][y_futuro].nome == "Fruta":
        mapa.matriz[x_futuro][y_futuro] = el.QuadradoVazio([x_futuro, y_futuro])
        mapa.matriz[x][y].tamanho += 1
        mapa.matriz[x][y].comeu = True



