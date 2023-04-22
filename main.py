from calculadora import Calculadora

calculadora = Calculadora()
while True:
    try:
        inteiro1 = int(input("Insira um numero inteiro:\n"))
        break
    except ValueError:
        print("O valor precisa ser um numero inteiro")

while True:
    try:
        inteiro2 = int(input("Insira um segundo numero inteiro:\n"))
        break
    except ValueError:
        print("O valor precisa ser um numero inteiro")

while True:
    try:    
        real = float(input("Agora insira um numero real:\n"))
        break
    except ValueError:
        print("O valor precia ser um numero real")    

calculadora.definir_valores(inteiro1, inteiro2, real)

print("O produto do dobro do primeiro com metade do segundo:", calculadora.produto())
print("A soma do triplo do primeiro com o terceiro:", calculadora.soma())
print("O terceiro elevado ao cubo:", calculadora.elevado_ao_cubo())