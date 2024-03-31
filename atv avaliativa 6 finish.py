'''
Com base na nova legislação da Previdência Brasileira, regulamentada pela Lei
Complementar nº 1354/2020 e pela Emenda à Constituição nº 49/2020, desenvolva um programa em
Python que solicite as seguintes informações de uma pessoa:

Sexo da pessoa (masculino/feminino).
Data de nascimento da pessoa (no formato DD/MM/AAAA).
Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as
seguintes regras:

Aposentadoria por Idade:

Homens podem se aposentar aos 65 anos de idade.
Mulheres podem se aposentar aos 62 anos de idade.
É necessário ter pelo menos 15 anos de contribuição.

Aposentadoria por Tempo de Contribuição:

Homens podem se aposentar após 35 anos de contribuição.
Mulheres podem se aposentar após 30 anos de contribuição.
Implemente o programa em Python para calcular a data de aposentadoria e exibi-la como resultado.

'''

from datetime import datetime

#Solicitar informações da pessoa
sexo = input("Informe o sexo da pessoa (masculino/feminino): ")
data_nascimento_str = input("Informe a data de nascimento da pessoa (no formato DD/MM/AAAA): ")
data_inicio_contribuicao_str = input("Informe a data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA): ")

#Converter as datas para objetos datetime
data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
data_inicio_contribuicao = datetime.strptime(data_inicio_contribuicao_str, '%d/%m/%Y')

#Calcular a data de aposentadoria
if sexo.lower() == 'masculino':
    idade_aposentadoria = 65
    tempo_contribuicao  = 35
else:
    idade_aposentadoria = 62
    tempo_contribuicao  = 30

data_aposentadoria_idade = data_nascimento(year=data_nascimento.year + idade_aposentadoria)
data_aposentadoria_contribuicao = data_inicio_contribuicao(year=data_inicio_contribuicao.year + tempo_contribuicao)

data_aposentadoria = max(data_aposentadoria_idade, data_aposentadoria_contribuicao)

#Mostre o resultado
print(f"A pessoa poderá se aposentar em: {data_aposentadoria.strptime('%d/%m/%Y')}")