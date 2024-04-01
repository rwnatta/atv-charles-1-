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


#Tempo em segundos
def calcular_tempo_segundos(horas, minutos):
    return horas * 3600 + minutos * 60

#Velocidade média
def calcular_velocidade_media(distancia, tempo_segundos):
    return distancia / (tempo_segundos / 3600)

#Custo da viagem com combustível
def calcular_custo_viagem(litros_combustivel, preco_litro):
    return litros_combustivel * preco_litro

#Desempenho do carro
def calcular_desempenho_carro(distancia, litros_combustivel, custo_viagem):
    km_por_litro    = distancia / litros_combustivel
    litros_por_hora = litros_combustivel / (tempo_segundos / 3600)
    custo_por_km    = custo_viagem / distancia
    return km_por_litro, litros_por_hora, custo_por_km


hora_partida         = int(input("Hora de partida:  "))
minuto_partida       = int(input("Minuto de partida:  "))
hora_chegada         = int(input("Hora de chegada:  "))
minuto_chegada       = int(input("Minuto de chegada:  "))
segundos_parados     = int(input("Segundos parados para descanso:  "))
litros_combustivel   = float(input("Litros de combustível gastos:  "))
preco_litro          = float(input("Preço do litro de combustível (R$):  "))
distancia_percorrida = float(input("Distância percorrida (em Km):  "))

#Cálculos
tempo_segundos = calcular_tempo_segundos(hora_chegada - hora_partida, minuto_chegada - minuto_partida - (segundos_parados / 60))
velocidade_media_global = calcular_velocidade_media(distancia_percorrida, tempo_segundos)
custo_viagem = calcular_custo_viagem(litros_combustivel, preco_litro)
km_por_litro, litros_por_hora, custo_por_km = calcular_desempenho_carro(distancia_percorrida, litros_combustivel, custo_viagem)


print(f"Tempo de viagem: {tempo_segundos} segundos")
print(f"Velocidade média global: {velocidade_media_global} Km/h")
print(f"Custo da viagem com combustível: R$ {custo_viagem}")
print(f"Desempenho do carro - Km/l: {km_por_litro}, l/h: {litros_por_hora}, R$/Km: {custo_por_km}")


