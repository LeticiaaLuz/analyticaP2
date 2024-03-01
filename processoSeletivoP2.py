# >>>>> QUESTÃO 1 <<<<< #

# Funcao para pegar o horario no formato certo do input
def pegarHorario():
    while True:
        horario = input('\nInforme o horario no formato(hh:mm) -> ')
        if (horario == 'f'): # Finalizar o programa
            print('\nFim...\n')
            return None
        
        elif (len(horario) != 5) or (horario[2] != ':'): # Verifica se as estradas estão no formato de horas
            print('\nInput inválido!\n')
            
        
        elif (horario[0:2].isdigit() and horario[3:5].isdigit()):
            horas = int(horario[0:2])
            minutos = int(horario[3:5])
            
            if ((0 <= horas <= 23) and (0 <= minutos <= 59)):
                return horas, minutos
            else: # Verifica se o horário está no formato 24hrs
                print('\nInput inválido!\n')
                
        else:
            print('\nInput inválido!\n')
            
    


# FORMA 1 DE RESOLUÇÃO:
# formula utilizada; angulo = (|11*minutos - 60*horas|)/2
            
# Funcao que vai calcular o angulo           
def calcularMenorAnguloFormula():
    while True:
        horario = pegarHorario()
        if horario is None:
            return 0
        else:
            horas, minutos = horario

        if (horas > 12): # Passa as horas para o intervalo de 0-12
            horas = horas - 12
        
        angulo = abs(11*minutos/2 - 30*horas)
        

        if (angulo > 180): # Pega o menor angulo
            angulo = 360 - angulo
            
        print(f'\nO menor ângulo é de {angulo}°\n')


# SEGUNDA FORMA DE RESOLUÇÃO DA QUESTÃO 1:
# angulo = (o quanto o ponteiro das horas andou) - (o quanto o ponteiro dos minutos andou) 
        
#def calcularMenorAngulo():
#    while True:

#        horario = pegarHorario()
#        if horario is None:
#            return 0
#        else:
#            horas, minutos = horario
        
#        if (horas > 12):
#            horas = horas - 12

#        angulo = abs((horas*30) - (minutos*6))
        

#        if (angulo > 180):
#            angulo = 360 - angulo
   
#        print(f'\nO menor ângulo é de {angulo}°\n')

# >>>>> QUESTÃO 2 <<<<< #

# Funcao para pegar a posicao inical e final no formato certo do input
def pegarPosicoes():
    while True: 
        
        posicoes = input('\nDigite a posicao inicial e final do cavalo: ')
        
        if posicoes == 'f': # Finalizar o programa
            print('\nFim...\n')
            return None
        
        elif len(posicoes) != 5 or posicoes[2] != ' ': # # Verifica se a entrada está no formato desejado
            print('\nInput inválido!\n')
        
        else:
            # Define listas de colunas e linhas do tabuleiro de xadrez
            colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
        
            if (posicoes[0] not in colunas or posicoes[1] not in linhas or
                posicoes[3] not in colunas or posicoes[4] not in linhas): # Verifica se as posicoes estão com valores presentes nas listas acima
                print('\nInput inválido!\n')
        
            else:
                return posicoes

def movimentarCavalo():
    while True:
        posicoes = pegarPosicoes()

        if posicoes is None:
            return 0

        # Separa a string. Divindo ela em posicao inicial e final              
        posicoes = posicoes.split(sep=" ")
        posicaoInicial, posicaoFinal = posicoes

        # Pega as colunas e linhas das posições inicial e final
        colunaInicial = posicaoInicial[0]
        linhaInicial = int(posicaoInicial[1])
        
        colunaFinal = posicaoFinal[0]
        linhaFinal = int(posicaoFinal[1])

        colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        colunaInicialIndice = colunas.index(colunaInicial)
        colunaFinalIndice = colunas.index(colunaFinal)
        
        # Condicoes para as posicoes serém válidas
        if (((abs(colunaFinalIndice - colunaInicialIndice) == 2) and (abs(linhaFinal - linhaInicial) == 1)) or\
                 ((abs(colunaFinalIndice - colunaInicialIndice) == 1) and (abs(linhaFinal - linhaInicial) == 2))):
            
            print('\nVÁLIDO\n')
        
        else:
            print('\nINVÁLIDO\n')
       
  

# >>>>> QUESTÃO 3 <<<<< #

# Funcao para pegar o valor no formato certo do input
def pegarValor():
    while True:

        valor = input('\nDigite o valor para ser decomposto: ')

        if ('.' in valor): # Verifica se o valor contém um ponto decimal
            inteiro, parteDecimal = valor.split(sep='.') # Divide a string em parte inteira e decimal
            
            if ((len(parteDecimal)==2) and (inteiro.isdigit()) and (parteDecimal.isdigit())): # Verifica se são dígitos e se a parte decimal tem 2 casas
                return valor
            
            else:
                print('\nInput inválido!\n')

        else:
            print('\nInput inválido!\n')

# Função para calcular o troco em notas e moedas
def calcularTroco():
    valor = pegarValor()
    valor = float(valor)

    # Listas de valores das notas e moedas
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    
    # Parte das notas
    print("\nNOTAS:")
    for elemento in notas:
        # Calcula a quantidade de notas necessárias
        quantidadeNotas = int(valor // elemento)
        valor = valor - quantidadeNotas*elemento
        nota = float(elemento)
        print(f'{quantidadeNotas} nota(s) de R$ {nota:.2f}')
        


    # Parte das moedas
    print("\nMOEDAS:")
    for elemento in moedas:
        if elemento == 0.01:
            # Para as moedas de 1 centavo, n foi utilizado o resto para evitar erros
            quantidadeMoedas = int(valor / elemento)
            valor = valor - quantidadeMoedas*elemento
            valor = round(valor, 2)
            moeda = float(elemento)
            print(f'{quantidadeMoedas} moeda(s) de R$ {moeda:.2f}')
        else:
            # Calcula a quantidade de moedas necessárias para os demais
            quantidadeMoedas = int(valor // elemento)
            valor = valor - quantidadeMoedas*elemento
            valor = round(valor, 2)
            moeda = float(elemento)
            print(f'{quantidadeMoedas} moeda(s) de R$ {moeda:.2f}')


        
    
    print('\n')
    return 0

# >>>>> QUESTÃO 4 <<<<< #

# Função para contar a frequência de números inseridos pelo usuário
def frequenciaDeNumeros():
    
    numerosContados = {}
    # Loop para solicitar os números ao usuário
    while True:
        numero = input("Digite um inteiro: ")
        if (numero == 'f'): # Finalizar o programa
            print('\nFim...')
            break
        
        elif (numero.isdigit()): # Verifica se a entrada é um número inteiro
            numero = int(numero)
            if numero in numerosContados: # Verifica se o número já está no dicionário
                numerosContados[numero] = numerosContados[numero] + 1 # Se estiver incrementa o valor 
            else:
                numerosContados[numero] = 1 # Caso não esteja vai ser adiconado ao diconario com o valor = 1

    for numero in numerosContados: # Printar na tela
        if (numerosContados[numero] == 1):
            print(f'O número {numero} apareceu 1 vez')
        else:
            print(f'O número {numero} apareceu {numerosContados[numero]} vezes')
    print('\n')        

print('\n> Questão 1 - Calculadora de ângulo entre ponteiros do relógio. <\n')
calcularMenorAnguloFormula()
print('\n> Questão 2 - Movimentação do cavalo no xadrez. <\n')
movimentarCavalo()
print('\n> Questão 3 - Calculadora de troco. <\n')
calcularTroco()
print('\n> Questão 4 - Frequência de números. <\n')
frequenciaDeNumeros()
