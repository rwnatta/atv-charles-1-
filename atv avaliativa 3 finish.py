'''
Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo.
Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada
(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto
(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km):

Após receber os dados, o programa informa dados típicos de um computador de bordo: 

a) o tempo de viagem (em segundos).
b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h).
c) o custo da viagem com combustível (em R$).
d) o desempenho do carro (em Km/l, l/h e R$/Km).

'''


hora_inicial, minuto_inicial = (input('Momento Inicial da partida: ')).split(':   ')
hora_final, minuto_final     = (input('Momento de Chegada: ')).split(':   ')
segundos_parados             = int(input ('segundos parados para descanso: '))
litros_combustivel           = float(input('Número de combustível gasto (em litros): '))
preco_litro_combustivel      = float(input('Preço do litro de combustível (em R$):  '))
distancia_percorrida         = float(input('Distância percorrida (em Km): '))

#CONVERSÃO DAS VARIAVEIS PRA INTEIRO
#TEMPO DA VIAGEM

hora_inicial   = int(hora_inicial)
minuto_inicial = int(minuto_inicial)
hora_final     = int(hora_final)
minuto_final   = int(minuto_final)
tempo_viagem   = ((hora_inicial * 3600)-(hora_final * 3600))-((minuto_inicial * 60)-(minuto_final * 60))
tempo_viagem_com_descanso = tempo_viagem + segundos_parados

#VELOCIDADE MÉDIA GLOBAL EM MOVIMENTO

vel_media_global    = distancia_percorrida / (tempo_viagem_com_descanso / 3600)
vel_media_movimento = distancia_percorrida / ((tempo_viagem + segundos_parados) / 3600)

vel_media_global    = distancia_percorrida / (tempo_viagem / 3600)
vel_media_movimento = distancia_percorrida / ((tempo_viagem + segundos_parados) / 3600)

#O CUSTO DA VIAGEM COM COMBUSTIVEL
custo_viagem = preco_litro_combustivel * litros_combustivel

#O DESEMPENHO DO CARRO
km_l = litros_combustivel / distancia_percorrida
l_h  = litros_combustivel / ((tempo_viagem - segundos_parados) / 3600)
r_km = (litros_combustivel * preco_litro_combustivel) / distancia_percorrida


print(f"O tempo de viagem foi: {tempo_viagem_com_descanso} segundos.")
print(f"A velocidade média  global foi", round(vel_media_global, 2),"(Km/h) e a velocidade média em movimento foi", round(vel_media_movimento, 2),"(Km/h).")
print(f"O custo da viagem com combustível foi de: R$", round(custo_viagem, 2),"." )
print(f"O Desempenho do carro foi de: Consumo médio:", round(km_l, 2), "Km/l, Consumo por hora:", round(l_h, 2), "l/h, Custo por Km:", round(r_km, 2), "R$/Km")