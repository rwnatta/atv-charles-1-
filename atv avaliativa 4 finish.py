'''
O número de dias decorridos entre duas datas é importante em uma infinidade de
situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial e mês
inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre
as datas (considere que o ano não é bissexto).

Exemplos:
02 de 05 até 03 de 05 - 1 dia.
27 de 04 até 03 de 05 - 6 dias.
03 de 02 até 03 de 05 - 79 dias.

Não esquecer de verificar se a data inicial é menor ou igual à data final.

'''

# Receber os valores do usuário
dia_inicial = int(input("Digite o dia inicial: "))
mes_inicial = int(input("Digite o mês inicial: "))
dia_final   = int(input("Digite o dia final: "))
mes_final   = int(input("Digite o mês final: "))

# Verificar se a data inicial é menor ou igual à data final
if mes_inicial > mes_final or (mes_inicial == mes_final and dia_inicial > dia_final):
    print("Data inicial deve ser menor ou igual à data final.")
else:
    
    #Calcular o número de dias decorridos
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_dias = 0

    #Somar os dias dos meses completos entre as datas
    for mes in range(mes_inicial, mes_final):
        total_dias += dias_por_mes[mes]

    #Adicionar os dias do mês inicial e final
    total_dias = total_dias - dia_inicial + dia_final

    #Mostre o resultado
    print(f"O número de dias entre as datas é: {total_dias} dias.")