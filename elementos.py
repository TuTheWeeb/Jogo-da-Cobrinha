

class Quadrado():
    def __init__(self):
        self.nome = "Quadrado"

    def __str__(self):
        return self.nome

class Cobra(Quadrado):
    def __init__(self):
        self.nome = "Cobra"

class Parede(Quadrado):
    def __init__(self):
        self.nome = "Parede"

class Comida(Quadrado):
    def __init__(self):
        self.nome = "Comida"
