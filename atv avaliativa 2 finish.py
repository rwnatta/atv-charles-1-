'''
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor
corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de
cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$
0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

'''

import sys

valor = float(input('Informe um valor decimal positivo:  '))

valor = float(input('Informe um valor do saque: R$  '))
valor = round(valor, 2)

cedulas_100 = int(valor // 100)
valor  %= 100

cedulas_50  = int(valor // 50)
valor  %= 50

cedulas_20  = int(valor // 20)
valor  %= 20

cedulas_10  = int(valor // 10)
valor  %= 10

cedulas_5   = int(valor // 5)
valor  %= 5

cedulas_2   = int(valor // 2)
valor  %= 2

moedas_1    = int(valor // 1)
valor  %= 1

moedas_050  = int(valor // 0.5)
valor  %= 0.5

moedas_025  = int(valor // 0.25)
valor  %= 0.25

moedas_010  = int(valor // 0.1)
valor  %= 0.1

moedas_005  = int(valor // 0.05)
valor  %= 0.05

moedas_001  = round(valor * 100)

print('Serão usadas as seguintes cédulas: ')

print('Cédulas: ')
print('R$ 100.00:', cedulas_100, 'cédulas')
print('R$ 50.00:' , cedulas_50,  'cédulas')
print('R$ 20.00:' , cedulas_20,  'cédulas')
print('R$ 10.00:' , cedulas_10,  'cédulas')
print('R$ 5.00:'  , cedulas_5,   'cédulas')
print('R$ 2.00:'  , cedulas_2,   'cédulas')

print('Moedas: ')
print('R$ 1.00:'  , moedas_1,    'moedas')
print('R$ 0.50:'  , moedas_050,  'moedas')
print('R$ 0.25:'  , moedas_025,  'moedas')
print('R$ 0.10:'  , moedas_010,  'moedas')
print('R$ 0.05:'  , moedas_005,  'moedas')
print('R$ 0.01:'  , moedas_001,  'moedas')