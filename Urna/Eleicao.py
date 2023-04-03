#Função para contar votos da eleição
def Contagem_de_Votos(votos, candidatos, qtd_votou_candidato, quantidade_eleitores, nulo, branco):
    qtd_votou = qtd_votou_candidato
    qtd_eleitores = quantidade_eleitores
    empate = 0
    venceu = 0
    votos_cada = []
    for chave, valor in votos.items():
        if chave != -1 and chave != -2:
            quantidade = votos[chave]
            quantidade = quantidade[2]
            votos_cada.append(quantidade)
    for item in votos_cada:
        if item > venceu:
            venceu = item
        elif item == venceu:
            empate = item
    if empate == venceu and empate != 0:
        print('Ocorreu um empate entre os candidatos!')
    else:
        for chave, valor in votos.items():
            if venceu in valor and chave != -1 and chave != -2:
                print()
                print()
                print(f'O novo eleito a {candidatos} foi {valor[0]} com {venceu} votos')
    Ranking_Candidatos(votos, venceu, votos_cada, qtd_votou, qtd_eleitores, candidatos, nulo, branco)

#Exibição de cada candidato com suas quantidades de votos
def Ranking_Candidatos(votos, venceu, votos_cada, qtd_votou, qtd_eleitores, candidatos, nulo, branco):
    nome_ranking = candidatos.upper()
    print()
    print(f'RANKING DO RESULTADO PARA {nome_ranking}')
    print('-' * 81)
    print(10 * ' ', 'NOME', ' ' * 18,'| Partido | Total de votos | % votos validos |')

    votos_cada.sort(reverse=True)
    soma_valido = 0
    
    if len(votos) != 2:
        while votos_cada != []:
            for chave, valor in votos.items():
                if chave != -1 and chave != -2:
                    voto_max = votos[chave]
                    voto_max = voto_max[2]
                    if voto_max in votos_cada and venceu == voto_max:
                        soma_valido += voto_max
                        porcento = (venceu / qtd_eleitores) * 100
                        print(('-' * 35) + '|' + ('-' * 9) + '|' + ('-' * 16) + '|' + ('-' * 17) + '|')
                        print(f'{valor[0]:<{tamanho_nome}} ', '|', f'{valor[1]:>8}', ' ',
                              '|', f'{valor[2]:>15}', ' ', '|',f'{porcento:>15}%', ' ', '|', sep='')
                        votos_cada.remove(voto_max)
                        if votos_cada != []:
                            venceu = votos_cada[0]
        print('-' * 81)
        print(f'Total de votos: {qtd_votou}')
        print(f'Total de votos válidos e %: {soma_valido} com {(soma_valido/qtd_eleitores)*100}%')
        print(f'Total de brancos e %: {branco} com {(branco/qtd_eleitores)*100}%')
        print(f'Total de nulos e %: {nulo} com {(nulo/qtd_eleitores)*100}%')
    else:
        print('-' * 81)
        print()
        print(f'Não existe candidatos a {candidatos} nesta eleição')
        print()
        print('-' * 81)
        print(f'Total de votos: {qtd_votou}')
        print(f'Total de votos válidos e %: {soma_valido} com ({(soma_valido/qtd_eleitores)*100}%)')
        print(f'Total de brancos e %: {branco} com ({(branco/qtd_eleitores)*100}%)')
        print(f'Total de nulos e %: {nulo} com ({(nulo/qtd_eleitores)*100}%)')
        print('-' * 81)


#Tamanho disponivel para o nome dos candidatos.
tamanho_nome = 34

#Tamanho disponivel para os nomes dos partidos.
tamanho_nome_partido = 5

#Tamanho disponivel para o numero de cada cadidato.
tamanho_numero_candidato = 3

#Quantidade de votação para cada poder hierarquico.
votos_prefeito = 0
votos_vereador = 0
votos_deputado_estadual = 0
votos_governador = 0
votos_deputado_federal = 0
votos_senador = 0
votos_presidente = 0

#Dicionario com nome, quantidade de votos e nome do partido de cada candidato.
prefeitos = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
vereadores = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
deputados_estaduais = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
governadores = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
deputados_federais = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
senadores = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}
presidentes = {-1: ['Voto em branco', 0], -2: ['Voto nulo', 0]}

#Dicionario com todos os partidos e quantidades de cada um.
partidos = {}

#Dicionario com o nome e cpf de cada eleitor.
eleitores = {}

#Quantidade de eleitores
quantidade_eleitores = 0

#Os valores com a quantidade de partidos elegidos na eleição
elegidos = []

#Continuar elegindo um candidato na eleição
continuar_elegindo_candidato = ''

#continuar adicionando eleitor para a votação 
continuar_cadastrando_eleitor = ''

#quantidades de votos para cada candidatamento
qtd_votou_presidente = 0
qtd_votou_senador = 0
qtd_votou_deputado_federal = 0
qtd_votou_governador = 0
qtd_votou_deputado_estadual = 0
qtd_votou_vereador = 0
qtd_votou_prefeito = 0

#Voto em nulo
nulo_prefeito = 0
nulo_vereadores = 0
nulo_deputados_estaduais = 0
nulo_governador = 0
nulo_deputados_federais = 0
nulo_senadores = 0
nulo_presidente = 0

#Voto em branco
branco_prefeito = 0
branco_vereadores = 0
branco_deputados_estaduais = 0
branco_governador = 0
branco_deputados_federais = 0
branco_senadores = 0
branco_presidente = 0

print()
print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++')
print()
print('1. Cadastrar Candidatos')
print('2. Cadastrar Eleitores')
print('3. Votar')
print('4. Apurar Resultados')
print('5. Relatório e Estatísticas')
print('6. Encerrar')
print()

opcao = int(input('Opção escolhida: '))
while opcao != 6:
    #Cadastrar Candidatos
    if opcao == 1:

        print()
        print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO PARA CANDIDATOS +++++++')
        print()
        print('1. Cadastrar Prefeitos')
        print('2. Cadastrar Vereadores')
        print('3. Cadastrar Deputados Estaduais')
        print('4. Cadastrar Governadores')
        print('5. Cadastrar Deputados Federais')
        print('6. Cadastrar Senadores')
        print('7. Cadastrar Presidentes')
        print()

        opcao_candidato = int(input('Opção escolhida: '))
        continua_candidatando = ''

        #Cadastrar Candidatos a Prefeito
        if opcao_candidato == 1 and continua_candidatando != 'NÃO':
            qtd_prefeito = int(input('Quantidade de eleitores a prefeitura: '))
            
            for _ in range(qtd_prefeito):
                nome_candidato = input('Nome do Prefeito: ').upper()  #Nome do Prefeito
                
                n_candidato = int(input('Nº do Prefeito: '))   #Numero do Prefeito
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Prefeito

                #Adicionar ao cargo para prefeito.
                if n_candidato not in prefeitos and n_candidato > 0:
                    prefeitos[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in prefeitos:
                    qtd_prefeito += 1

                
        #Cadastrar Candidatos a Vereador
        elif opcao_candidato == 2 and continua_candidatando != 'NÃO':
            qtd_vereador = int(input('Quantidade de eleitores a Vereador: '))
            
            for _ in range(qtd_vereador):
                nome_candidato = input('Nome do Vereador: ').upper()  #Nome do Vereador
                
                n_candidato = int(input('Nº do Vereador: '))   #Numero do Vereador
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Vereador

                #Adicionar ao cargo para vereador.
                if n_candidato not in vereadores and n_candidato > 0:
                    vereadores[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in vereadores:
                    qtd_vereador += 1

                
        #Cadastrar Candidatos a Deputado Estadual
        elif opcao_candidato == 3 and continua_candidatando != 'NÃO':
            qtd_deputado_estadual = int(input('Quantidade de eleitores a Deputado Estadual: '))
            
            for _ in range(qtd_deputado_estadual):
                nome_candidato = input('Nome do Deputado Estadual: ').upper()  #Nome do Deputado Estadual
                
                n_candidato = int(input('Nº do Deputado Estadual: '))   #Numero do Deputado Estadual
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Deputado Estadual

                #Adicionar ao cargo para deputado estadual.
                if n_candidato not in deputados_estaduais and n_candidato > 0:
                    deputados_estaduais[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in deputados_estaduais:
                    qtd_deputado_estadual += 1

                
        #Cadastrar Candidatos a Governador
        elif opcao_candidato == 4 and continua_candidatando != 'NÃO':
            qtd_governador = int(input('Quantidade de eleitores ao Governo: '))
            
            for _ in range(qtd_governador):
                nome_candidato = input('Nome do Governador: ').upper()  #Nome do Governador
                
                n_candidato = int(input('Nº do Governador: '))   #Numero do Governador
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Governador

                #Adicionar ao cargo para governador.
                if n_candidato not in governadores and n_candidato > 0:
                    governadores[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in governadores:
                    qtd_governador += 1

                
        #Cadastrar Candidatos a Deputado Federal
        elif opcao_candidato == 5 and continua_candidatando != 'NÃO':
            qtd_deputado_federal = int(input('Quantidade de eleitores a Deputado Federal: '))
            
            for _ in range(qtd_deputado_federal):
                nome_candidato = input('Nome do Deputado Federal: ').upper()  #Nome do Deputado Federal
                
                n_candidato = int(input('Nº do Deputado Federal: '))   #Numero do Deputado Federal
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Deputado Federal

                #Adicionar ao cargo para deputado federal.
                if n_candidato not in deputados_federais and n_candidato > 0:
                    deputados_federais[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in deputados_federais:
                    qtd_deputado_federal += 1

                
        #Cadastrar Candidatos a Senador
        elif opcao_candidato == 6 and continua_candidatando != 'NÃO':
            qtd_senador = int(input('Quantidade de eleitores ao Senado: '))
            
            for _ in range(qtd_senador):
                nome_candidato = input('Nome do Senador: ').upper()  #Nome do Senador
                
                n_candidato = int(input('Nº do Senador: '))   #Numero do Senador
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Senador

                #Adicionar ao cargo para senador.
                if n_candidato not in senadores and n_candidato > 0:
                    senadores[n_candidato] = [nome_candidato, partido_candidato, 0]

                elif n_candidato in senadores:
                    qtd_senador += 1

                
        #Cadastrar Candidatos a Presidente
        elif opcao_candidato == 7 and continua_candidatando != 'NÃO':
            qtd_presidente = int(input('Quantidade de eleitores a presidencia: '))
            
            for _ in range(qtd_presidente):
                nome_candidato = input('Nome do Presidente: ').upper()  #Nome do Presidente
                
                n_candidato = int(input('Nº do Presidente: '))   #Numero do Presidente
                
                partido_candidato = input('Nome do Partido: ').upper()  #Partido do Presidente

                #Adicionar ao cargo para presidente.
                if n_candidato not in presidentes and n_candidato > 0:
                    presidentes[n_candidato] = [nome_candidato, partido_candidato, 0]
                    
                elif n_candidato in presidentes:
                    qtd_presidente += 1

        continua_candidatando = input('Continuar candidatando: ')


    #Cadastrar Eleitores
    elif opcao == 2:

        #Enquanto o usuario não digitar(NÃO), continue digitando os eleitores
        while continuar_cadastrando_eleitor != 'NÃO':
            nome_eleitor = input('Nome do eleitor: ')
            cpf_eleitor = int(input('CPF do eleitor: '))
            
            if cpf_eleitor not in eleitores:
                eleitores[cpf_eleitor] = nome_eleitor
                quantidade_eleitores += 1
                
            elif cpf_eleitor in eleitores:
                print('Este eleitor ja foi adicionado.')

            #Se a resposta for não, digite(NÃO) para encerrar    
            continuar_cadastrando_eleitor = input('Adicionar outro eleitor? ')
        continuar_cadastrando_eleitor = ''



    #Votar
    elif opcao == 3:
        
        
        confirma = ''
        for _ in range(quantidade_eleitores):

            if len(prefeitos) != 2:
                qtd_votou_prefeito += 1
                
                #Votação para Prefeito
                while confirma != 'confirma':
                    votacao_prefeito = int(input('Voto para Prefeito: '))
                    if votacao_prefeito in prefeitos:        
                        voto = prefeitos[votacao_prefeito]
                        if votacao_prefeito != -1 and votacao_prefeito != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_prefeito not in prefeitos:
                        print('Voto ao candidato inexistente!')
                        
                if votacao_prefeito != -1 and votacao_prefeito != -2:
                    voto[2] += 1
                else:
                    voto[1] += 1
                    if votacao_prefeito == -1:
                        nulo_prefeito +=1
                    else:
                        branco_prefeito += 1
                    
                prefeitos[votacao_prefeito] = voto
                votos_prefeito += 1
                confirma = ''
                
            if len(vereadores) != 2:
                qtd_votou_vereador += 1
                
                #Votação para Vereador
                while confirma != 'confirma':
                    votacao_vereador = int(input('Voto para Vereador: '))
                    if votacao_vereador in vereadores:
                        voto = vereadores[votacao_vereador]
                        if votacao_vereador != -1 and votacao_vereador != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_vereador not in vereadores:
                        print('Voto ao candidato inexistente!')
                        
                if votacao_vereador != -1 and votacao_vereador != -2:
                    voto[2] += 1
                else:
                    voto[1] += 1
                    if votacao_vereador == -1:
                        nulo_vereadores +=1
                    else:
                        branco_vereadores += 1
                    
                vereadores[votacao_vereador] = voto
                votos_vereador += 1
                confirma = ''
                
            if len(deputados_estaduais) != 2:
                qtd_votou_deputado_estadual += 1
                
                #Votação para Deputado Estadual
                while confirma != 'confirma':
                    votacao_deputado_estadual = int(input('Voto para Deputado Estadual: '))
                    if votacao_deputado_estadual in deputados_estaduais:        
                        voto = deputados_estaduais[votacao_deputado_estadual]
                        if votacao_deputado_estadual != -1 and votacao_deputado_estadual != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_deputado_estadual not in deputados_estaduais:
                        print('Voto ao candidato inexistente!')
                        
                if votacao_deputado_estadual != -1 and votacao_deputado_estadual != -2:
                    voto[2] += 1
                else:
                    voto[1] += 1
                    if votacao_deputado_estadual == -1:
                        nulo_deputados_estaduais +=1
                    else:
                        branco_deputados_estaduais += 1
                    
                deputados_estaduais[votacao_deputado_estadual] = voto
                votos_deputado_estadual += 1
                confirma = ''

            if len(governadores) != 2:
                qtd_votou_governador += 1
                
                #Votação para Governador
                while confirma != 'confirma':
                    votacao_governador = int(input('Voto para Governador: '))
                    if votacao_governador in governadores:
                        voto = governadores[votacao_governador]
                        if votacao_governador != -1 and votacao_governador != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_governador not in governadores:
                        print('Candidato inexistente!')

                if votacao_governador != -1 and votacao_governador != -2:
                    voto[2] += 1
                    
                else:
                    voto[1] += 1
                    if votacao_governador == -1:
                        nulo_governador +=1
                    else:
                        branco_governador += 1
                    
                governadores[votacao_governador] = voto
                votos_governador += 1
                confirma = ''

            if len(deputados_federais) != 2:
                qtd_votou_deputado_federal += 1
                
                #Votação para Deputado Federal
                while confirma != 'confirma':
                    votacao_deputado_federal = int(input('Voto para Deputado Federal: '))
                    if votacao_deputado_federal in deputados_federais:        
                        voto = deputados_federais[votacao_deputado_federal]
                        if votacao_deputado_federal != -1 and votacao_deputado_federal != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_deputado_federal not in deputados_federais:
                        print('Voto ao candidato inexistente!')
                        
                if votacao_deputado_federal != -1 and votacao_deputado_federal != -2:
                    voto[2] += 1
                else:
                    voto[1] += 1
                    if votacao_deputado_federal == -1:
                        nulo_deputados_federais +=1
                    else:
                        branco_deputados_federais += 1
                    
                deputados_federais[votacao_deputado_federal] = voto
                votos_deputado_federal += 1
                confirma = ''

            if len(senadores) != 2:
                qtd_votou_senador += 1
                
                #Votação para Senador
                while confirma != 'confirma':
                    votacao_senadores = int(input('Voto para Senador: '))
                    if votacao_senadores in senadores:        
                        voto = senadores[votacao_senadores]
                        if votacao_senadores != -1 and votacao_senadores != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                        
                    elif votacao_senadores not in senadores:
                        print('Voto ao candidato inexistente!')
                        
                if votacao_senadores != -1 and votacao_senadores != -2:
                    voto[2] += 1
                else:
                    voto[1] += 1
                    if votacao_senadores == -1:
                        nulo_senadores +=1
                    else:
                        branco_senadores += 1
                    
                senadores[votacao_senadores] = voto
                votos_senador += 1
                confirma = ''

            if len(presidentes) != 2:
                qtd_votou_presidente += 1
                
                #Votação para Presidente
                while confirma != 'confirma':
                    votacao_presidente = int(input('Voto para Presidente: '))
                    if votacao_presidente in presidentes:
                        voto = presidentes[votacao_presidente]
                        if votacao_presidente != -1 and votacao_presidente != -2:
                            print(f'Nome do candidato: {voto[0]} do {voto[1]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                        else:
                            print(f'{voto[0]}')
                            confirma = input('Digite (confirma) para confimar seu voto: ')
                            
                    elif votacao_presidente not in presidentes:
                        print('Candidato inexistente!')

                if votacao_presidente != -1 and votacao_presidente != -2:
                    voto[2] += 1
                    
                else:
                    voto[1] += 1
                    if votacao_presidente == -1:
                        nulo_presidente +=1
                    else:
                        branco_presidente += 1
                    
                presidentes[votacao_presidente] = voto
                votos_presidente += 1
                confirma = ''

        #Caso não teja eleitores para a votação
        if quantidade_eleitores == 0:
            print()
            print('-' * 62)
            print('NENHUM ELEITOR CADASTRADO ATUALMENTE PARA FAZER ESTA VOTAÇÃO!!')
            print('-' * 62)



    #Apurar Resultados
    elif opcao == 4:

        #Contagem dos votos para PRESIDENTE
        Contagem_de_Votos(presidentes, 'Presidente', qtd_votou_presidente, quantidade_eleitores, nulo_presidente, branco_presidente)

        #Contagem dos votos para GOVERNADOR
        Contagem_de_Votos(governadores, 'Governador', qtd_votou_governador, quantidade_eleitores, nulo_governador, branco_governador)

        #Contagem dos votos para SENADORES
        Contagem_de_Votos(senadores, 'Senador', qtd_votou_senador, quantidade_eleitores, nulo_senadores, branco_senadores)

        #Contagem dos votos para DEPUTADOS FEDERAIS
        Contagem_de_Votos(deputados_federais, 'Deputado Federal', qtd_votou_deputado_federal, quantidade_eleitores, nulo_deputados_federais, branco_deputados_federais)

        #Contagem dos votos para DEPUTADOS ESTADUAIS
        Contagem_de_Votos(deputados_estaduais, 'Deputado Estadual', qtd_votou_deputado_estadual, quantidade_eleitores, nulo_deputados_estaduais, branco_deputados_estaduais)

        #Contagem dos votos para VEREADORES
        Contagem_de_Votos(vereadores, 'Vereador', qtd_votou_vereador, quantidade_eleitores, nulo_vereadores, branco_vereadores)

        #Contagem dos votos para PREFEITOS
        Contagem_de_Votos(prefeitos, 'Prefeito', qtd_votou_prefeito, quantidade_eleitores, nulo_prefeito, branco_prefeito)



    #Relatório e Estatiscas
    elif opcao == 5:

        #Pocisao de cada eleitor
        posicao = 1

        print('-' * 66)
        print('NOME DOS ELEITORES')
        print('-' * 66)

        #Exibição de cada eleitor
        for valor in eleitores.values():
            print(f'{posicao}. {valor}')
            posicao += 1

        if posicao == 1:
            print('NÃO EXISTE NENHUM ELEITOR CADASTRADO ATUALMENTE PARA ESTA ELEIÇÃO!')
            print()

        #Adicionando os valores de cada partido que esta no dicionario(partidos) a uma lista.
        for valor in partidos.values():
            elegidos.append(valor)
            
        print('-' * 66)
        print('NOME DOS PARTIDOS')
        print('-' * 66)

        #Se estiver partidos cadastrado na eleição exiba.
        if posicao > 1:
            elegidos.sort(reverse=True)
            maior_partido = elegidos[0]
            menor_partido = elegidos[-1]
            for chave, valor in partidos.items():
                if maior_partido == valor:
                    print(f'Partido que mais elegiu {chave}')
                elif menor_partido == valor:
                    print(f'Partido que menos elegiu {chave}')

        #Se não tiver exiba uma mensagem que não a partidos cadastrado
        else:
            print('NÃO EXISTE NENHUM PARTIDO CADASTRADO ATUALMENTE PARA ESTA ELEIÇÃO!')
            print('-' * 66)

    #Encerrar  
    elif opcao == 6:
        
        #Finalização do Programa
        break

    print()
    print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++')
    print()
    print('1. Cadastrar Candidatos')
    print('2. Cadastrar Eleitores')
    print('3. Votar')
    print('4. Apurar Resultados')
    print('5. Relatório e Estatísticas')
    print('6. Encerrar')
    print()
    opcao = int(input('Opção escolhida: '))


#Exibição com o nome, numero, partido e cargo a concorrer de cada candidato de acordo com a sequencia de entradas dada pelo úsuario
'''print()
print()
print('-' * 25)
print('Prefeitos')
print('=' * 25)
print()
if len(prefeitos) != 2:
    for chave, valor in prefeitos.items():
        if chave != -1 and chave != -2:
            print('-' * 61)
            print(f'Nome: {valor[0]:<{tamanho_nome}} ', f' Numero: {chave:<{tamanho_numero_candidato}}', '|', f' Partido: {valor[1]:<{tamanho_nome_partido}}', '|', sep='')
else:
    print('Não existe candidatos a Prefeito nesta eleição')

print('-' * 25)
print()
print()
print('-' * 25)
print('Governadores')
print('=' * 25)
print()

if len(governadores) != 2:
    for chave, valor in governadores.items():
        if chave != -1 and chave != -2:
            print('-' * 61)
            print(f'Nome: {valor[0]:<{tamanho_nome}} ', f' Numero: {chave:<{tamanho_numero_candidato}}', '|', f' Partido: {valor[1]:<{tamanho_nome_partido}}', '|', sep='')
else:
    print('Não existe candidatos a Governador nesta eleição')

print('-' * 25)
print()
print()
print('-' * 25)
print('Presidentes')
print('=' * 25)
print()
if len(presidentes) != 2:
    for chave, valor in presidentes.items():
        if chave != -1 and chave != -2:
            print('-' * 61)
            print(f'Nome: {valor[0]:<{tamanho_nome}} ', f' Numero: {chave:<{tamanho_numero_candidato}}', '|', f' Partido: {valor[1]:<{tamanho_nome_partido}}', '|', sep='')

else:
    print('Não existe candidatos a Presidente nesta eleição')
print('-' * 25)
print()
'''
