'''
Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma
dos seus algarismos.

'''

num1 = int(input('Informe um número de 0 a 9999 que vai fazer a soma deles:  '))

import sys
if num1 > 9999 or num1 < 0:
    print ('O número informado é inválido')
    sys.exit()

soma = 0
soma + = num1 % 10
num1 //= 10
soma + = num1 % 10
num1 //=  10
soma + = num1 % 10
num1 //= 10
soma + = num1 % 10 

print(f'A soma dos números é: {soma}')
