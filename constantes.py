"""constantes para teste"""

#canvas e geometria
GAME_WIDTH = 800 #largura
GAME_HEIGHT = 800 #altura
CORRECAO = 100
MAPA_WIDTH = GAME_WIDTH - CORRECAO
MAPA_HEIGHT = GAME_HEIGHT - CORRECAO
PIXEL_CONTROL = 10 #inversamente proporcional ao tamanho do pixel. Aumente para aumentar a qnt de pixels 
HEIGHT_PROPORTIONS = int((MAPA_HEIGHT / PIXEL_CONTROL) - 1)
WIDTH_PROPORTIONS = int((MAPA_WIDTH / PIXEL_CONTROL) - 1)
BODY_PARTS = 3
VELOCIDADE = 230

#cores
#SNAKE_COLOR = "#00FF00" #verde
APPLE_COLOR = "#FF0000" #vermelho
LEMON_COLOR = "#73f461" #verde
ORANGE_COLOR = "#f4750f" #laranja
WALL_COLOR = "#47504a" #cinza
BACKGROUND_COLOR = "#263D42" #
