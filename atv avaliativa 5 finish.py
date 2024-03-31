'''
Em um estacionamento, as tarifas são as seguintes (cumulativas):

Até duas horas: R$ 8,00/hora ou fração;
Entre três e quatro horas: R$ 5,00/hora ou fração;
Horas seguintes: R$ 3,00/hora ou fração.
Depois de 12h, o custo passa a ser fixo: R$ 30,00.

Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
o valor a ser pago pelo responsável.

'''


#Ler o número de minutos que o veículo ficou no estacionamento
minutos = int(input("Informe o número de minutos que o veículo ficou no estacionamento:  "))

#Calcular o número de horas completas e a fração de hora
horas = minutos // 60
minutos_restantes = minutos % 60

#Aplicar as tarifas de acordo com as regras fornecidas
if horas < 2:
    valor_a_pagar = horas * 8
elif horas < 4:
    valor_a_pagar = 2 * 8 + (horas - 2) * 5
else:
    valor_a_pagar = 2 * 8 + 2 * 5 + (horas - 4) * 3

#Mostre o valor total a ser pago
print(f"O valor a ser pago pelo responsável é: R$ {valor_a_pagar:.2f}")