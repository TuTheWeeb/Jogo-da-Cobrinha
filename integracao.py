#pode ser interessante fazer a renderização como uma função vetorizada
#Nesse módulo vai a construção da janela em tk e renderização
import tkinter as tk

score = 0
direction = "down"
SPEED = 100

#criando a janela
window = tk.Tk()

#definições da janela
window.title("Jogo da Cobrinha")
window.resizable(False,False)

score_label = tk.Label(window, text="Score: ".format(score), font=("TimesNewRoman", 40), )
score_label.pack()

window.mainloop()