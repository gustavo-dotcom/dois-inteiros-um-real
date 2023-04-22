class Calculadora:
    def __init__(self):
        self.valores = [0, 0, 0]

    def definir_valores(self, inteiro1: int, inteiro2: int, real: float):
        self.valores = [inteiro1, inteiro2, real]

    def produto(self): 
        return (self.valores[0] * 2) * (self.valores[1] / 2)

    def soma(self):
        return (self.valores[0] * 3) + self.valores[2]

    def elevado_ao_cubo(self):
        return self.valores[2] ** 3