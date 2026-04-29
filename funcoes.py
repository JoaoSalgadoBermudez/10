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

def calcula_pontos_soma(dados_rolados):
    soma = 0
    i = 0

    while i < len(dados_rolados):
        soma = soma + dados_rolados[i]
        i = i + 1

    return soma 
def calcula_pontos_sequencia_baixa(dados_rolados):
    te1 = 0
    te2 = 0
    te3 = 0
    te4 = 0
    te5 = 0
    te6 = 0

    i = 0
    while i < len(dados_rolados):
        if dados_rolados[i] == 1:
            te1 = 1
        if dados_rolados[i] == 2:
            te2 = 1
        if dados_rolados[i] == 3:
            te3 = 1
        if dados_rolados[i] == 4:
            te4 = 1
        if dados_rolados[i] == 5:
            te5 = 1
        if dados_rolados[i] == 6:
            te6 = 1
        i = i + 1

    if te1 and te2 and te3 and te4:
        return 15
    if te2 and te3 and te4 and te5:
        return 15
    if te3 and te4 and te5 and te6:
        return 15

    return 0  

def calcula_pontos_sequencia_alta (dados_rolados):
    te1 = 0
    te2 = 0
    te3 = 0
    te4 = 0
    te5 = 0
    te6 = 0

    i = 0
    while i < len(dados_rolados):
        if dados_rolados[i] == 1:
            te1 = 1
        if dados_rolados[i] == 2:
            te2 = 1
        if dados_rolados[i] == 3:
            te3 = 1
        if dados_rolados[i] == 4:
            te4 = 1
        if dados_rolados[i] == 5:
            te5 = 1
        if dados_rolados[i] == 6:
            te6 = 1
        i = i + 1

    if te1 and te2 and te3 and te4 and te5:
        return 30
    if te2 and te3 and te4 and te5 and te6:
        return 30

    return 0 

def calcula_pontos_full_house (dados_rolados):
    te1 = 0
    te2 = 0
    te3 = 0
    te4 = 0
    te5 = 0
    te6 = 0

    soma = 0
    
    for face in dados_rolados:
        if face == 1:
            te1 +=1
        if face == 2:
            te2 +=1
        if face == 3:
            te3 +=1
        if face == 4:
            te4 +=1
        if face == 5:
            te5 +=1
        if face == 6:
            te6 +=1
        soma += face
    
    if 3 in [te1, te2, te3, te4, te5, te6]:
        if 2 in [te1, te2, te3, te4, te5, te6]:
            return soma
            
    return 0

def calcula_pontos_quadra (dados_rolados):
    te1 = 0
    te2 = 0
    te3 = 0
    te4 = 0
    te5 = 0
    te6 = 0

    soma = 0
    
    for face in dados_rolados:
        if face == 1:
            te1 +=1
        if face == 2:
            te2 +=1
        if face == 3:
            te3 +=1
        if face == 4:
            te4 +=1
        if face == 5:
            te5 +=1
        if face == 6:
            te6 +=1
        soma += face
    
    if te1 >= 4 or te2 >= 4 or te3 >= 4 or te4 >= 4 or te5 >= 4 or te6 >= 4:
        return soma
            
    return 0

def calcula_pontos_quina (dados_rolados):
    te1 = 0
    te2 = 0
    te3 = 0
    te4 = 0
    te5 = 0
    te6 = 0
    
    for face in dados_rolados:
        if face == 1:
            te1 +=1
        if face == 2:
            te2 +=1
        if face == 3:
            te3 +=1
        if face == 4:
            te4 +=1
        if face == 5:
            te5 +=1
        if face == 6:
            te6 +=1
    
    if te1 >= 5 or te2 >= 5 or te3 >= 5 or te4 >= 5 or te5 >= 5 or te6 >= 5:
        return 50
            
    return 0