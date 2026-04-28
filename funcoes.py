import random
def rolar_dados (numero_de_dados):
    lista = []
    i = 0
    while i < numero_de_dados:
        lista.append(random.randint(1,6))
        i += 1
    return lista


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novo_rolados = []
    i = 0

    while i < len(dados_rolados):
        if i != dado_para_guardar:
            novo_rolados.append(dados_rolados[i])
        i = i + 1

    dados_no_estoque.append(dados_rolados[dado_para_guardar])

    return [novo_rolados, dados_no_estoque]