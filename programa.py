import funcoes

cartela = {
    "regra_simples": {
        1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1
    },
    "regra_avancada": {
        "sem_combinacao": -1,
        "quadra": -1,
        "full_house": -1,
        "sequencia_baixa": -1,
        "sequencia_alta": -1,
        "cinco_iguais": -1
    }
}

funcoes.imprime_cartela(cartela)

rodada = 0
while rodada < 12:

    dados_rolados = funcoes.rolar_dados(5)
    print (f"Dados rolados: {dados_rolados}")

    dados_guardados = []
    print (f"Dados guardados: {dados_guardados}")

    print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    jogada = False
    r = 0
    
    while not jogada:
        comando = input()

        if comando == '1':
            print ("Digite o índice do dado a ser guardado (0 a 4):")
            dado_para_guardar = int(input())
        
            dados_guardados_dados_rolados = funcoes.guardar_dado(dados_rolados, dados_guardados, dado_para_guardar)
            dados_rolados = dados_guardados_dados_rolados [0]
            dados_guardados = dados_guardados_dados_rolados [1]

            print (f"Dados rolados: {dados_rolados}")
            print (f"Dados guardados: {dados_guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        
        elif comando == '2':
            print ("Digite o índice do dado a ser removido (0 a 4):")
            dado_para_remover = int(input())
            
            dados_guardados_dados_rolados = funcoes.remover_dado(dados_rolados, dados_guardados, dado_para_remover)
            dados_rolados = dados_guardados_dados_rolados [0]
            dados_guardados = dados_guardados_dados_rolados [1]
            
            print (f"Dados rolados: {dados_rolados}")
            print (f"Dados guardados: {dados_guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif comando == '3':
            if r >= 2:
                print ("Você já usou todas as rerrolagens.")
            
            else:
                dados_rolados = funcoes.rolar_dados (len(dados_rolados))
                r += 1

            print (f"Dados rolados: {dados_rolados}")
            print (f"Dados guardados: {dados_guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif comando == '4':
            funcoes.imprime_cartela(cartela)

            print (f"Dados rolados: {dados_rolados}")
            print (f"Dados guardados: {dados_guardados}")
            print ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif comando == '0':
            print ("Digite a combinação desejada:")
            c = False

            while not c:
                categoria = input()

                validas = ["1","2","3","4","5","6", "cinco_iguais","full_house","quadra", "sem_combinacao","sequencia_alta","sequencia_baixa"]

                if categoria in validas:

                    if categoria in cartela["regra_avancada"]:
                        utilizada = cartela["regra_avancada"][categoria] != -1
                    else:
                        utilizada = cartela["regra_simples"][int(categoria)] != -1

                    if utilizada:
                        print("Essa combinação já foi utilizada.")
                    else:
                        funcoes.faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                        jogada = True
                        c = True

                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print ("Opção inválida. Tente novamente.")

    rodada += 1

pontuacao_total = 0

funcoes.imprime_cartela(cartela)

for valor in cartela["regra_simples"].values():
    if valor != -1:
        pontuacao_total += valor

for valor in cartela ["regra_avancada"].values():
    if valor != -1:
        pontuacao_total += valor

soma_simples = 0

for valor in cartela["regra_simples"].values():
    if valor != -1:
        soma_simples += valor

if soma_simples >= 63:
    pontuacao_total += 35

print (f"Pontuação total: {pontuacao_total}")