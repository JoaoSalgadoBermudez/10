import random
def rolar_dados (numero_de_dados):
    lista = []
    i = 0
    while i < numero_de_dados:
        lista.append(random.randint(1,6))
        i += 1
    return lista