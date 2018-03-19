# -*- coding: UTF-8 -*-

def cadastro(numeros):
    print('Digite um número:')
    numero = input()
    numeros.append(numero)

def listar(numeros):
    print(numeros)

def maior(numeros):
    maior = max(numeros)
    print('O maior número é %s' %(maior))

def qntsvezes(numeros):
    primeiro_numero = numeros[0]
    contador = 0
    for teste in numeros:
        if(teste == primeiro_numero):
                contador += 1
    print('A quantidade de vezes que o primeiro número repete é: %s' %(contador))

def menu():
    escolha = ''
    numeros = []
    while (escolha != '0'):
        print('\nDigite a opção desejada:\n')
        print('[1] - Cadastro de números;\n')
        print('[2] - Retornar o maior elemento;\n')
        print('[3] - número de ocorrências do primeiro elemento da lista;\n')
        print('[4] - Média dos elementos;\n')
        print('[5] - Valor mais próximo da média dos elementos;\n')
        print('[6] - Soma dos elementos com valor negativo;\n')
        print('[7] - Quantidade de vizinhos iguais;\n')
        print('[8] - Listar todos os números;\n')
        print('[0] - Sair!\n')
        escolha = input()
        if (escolha == '1'):
            cadastro(numeros)
        if (escolha == '8'):
            listar(numeros)
        if (escolha == '2'):
            maior(numeros)
        if (escolha == '3'):
            qntsvezes(numeros)

menu()