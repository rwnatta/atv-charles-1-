'''
Desenvolva um código em Python que solicite ao usuário que informe os
comprimentos dos três lados de um triângulo. Em seguida, verifique se esses comprimentos podem
formar um triângulo. Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e classifiqueo quanto aos lados e aos ângulos.

a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo.
b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe
que não é possível formar um triângulo com esses lados.
c) Se for possível formar um triângulo, calcule os três ângulos do triângulo.
d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos
(agudo, obtuso ou retângulo).
e) Exiba a classificação do triângulo quanto aos lados e aos ângulos.


'''


import math

# Solicita ao usuário que insira os comprimentos dos três lados do triângulo
lado1 = float(input("Insira o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Insira o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Insira o comprimento do terceiro lado do triângulo: "))

# Verifica se os comprimentos fornecidos podem formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
   
    #Calcula os três ângulos do triângulo usando a Lei dos Cossenos
    angulo1 = round("math.degrees(math.acos((lado2*2 + lado3*2 - lado1*2)" / (2 * lado2 * lado3)), 2.
    angulo2 = round("math.degrees(math.acos((lado1*2 + lado3*2 - lado2*2)" / (2 * lado1 * lado3)), 2.
    angulo3 = round(180 - angulo1 - angulo2, 2)

    #Classifique o triângulo quanto aos lados e aos ângulos
    if lado1 == lado2 == lado3:
        tipo_lados = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"

    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        tipo_angulos = "Agudo"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        tipo_angulos = "Retângulo"
    else:
        tipo_angulos = "Obtuso"

    #Mostre a classificação do triângulo quanto aos lados e aos ângulos
    print(f"O triângulo é classificado como {tipo_lados} e {tipo_angulos}.")
else:
    print("Não é possível formar um triângulo com esses lados.")