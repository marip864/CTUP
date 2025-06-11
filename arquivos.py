import pandas as pd

qantidade_de_pontos = int(input("Digite a quantidade de pontos: "))

dados = { 'Pressão (P)': [],
         'Volume (V)': [],      
         'Temperatura (T)': [] }
# Coleta os dados de pressão, volume e temperatura

for _ in range(qantidade_de_pontos):
    pressao = float(input("digite a pressão: "))
    volume = float(input("digite o volume: "))
    temperatura = float(input("digite a temperatura: "))
    dados['Pressão (P)'].append(pressao)
    dados['Volume (V)'].append(volume)  
    dados['Temperatura (T)'].append(temperatura)

df = pd.DataFrame(dados)

df.to_csv('dados.csv', index=False)

arquivo_lido = pd.read_csv('dados.csv')
arquivo_lido = pd.to_excel('dados.xlsx', index=False)
print("Dados salvos com sucesso!")