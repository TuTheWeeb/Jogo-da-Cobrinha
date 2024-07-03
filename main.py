from tkinter import *

BACKGROUND_COLOR = "#263D42"
GAME_WIDTH = 700
GAME_HEIGHT = 700

window = Tk()
window.title("Jogo da Cobrinha")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window,
              text="Score: {}".format(score),
              font=("consolas", 40)
              )
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Update window making it render
window.update()

window.mainloop()
