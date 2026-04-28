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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    i = 0

    while i < len(dados_no_estoque):
        if i != dado_para_remover:
            novo_estoque.append(dados_no_estoque[i])
        i = i + 1

    dados_rolados.append(dados_no_estoque[dado_para_remover])

    return [dados_rolados, novo_estoque]


def calcula_pontos_regra_simples(dados_rolados):
    resultado = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    i = 0
    while i < len(dados_rolados):
        valor = dados_rolados[i]
        resultado[valor] = resultado[valor] + valor
        i = i + 1

    return resultado