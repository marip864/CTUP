import pandas as pd

quantidade_de_pontos = int(input("Digite a quantidade de pontos: "))

dados = { 'Pressão (P)': [],
         'Volume (V)': [],      
         'Temperatura (T)': [] }

for _ in range(quantidade_de_pontos):
    pressao = float(input("digite a pressão: "))
    volume = float(input("digite o volume: "))
    temperatura = float(input("digite a temperatura: "))
    dados['Pressão (P)'].append(pressao)
    dados['Volume (V)'].append(volume)  
    dados['Temperatura (T)'].append(temperatura)

df = pd.DataFrame(dados)

df.to_csv('dados.csv', index=False)

df = pd.read_csv('dados.csv')

pressoes = df['Pressão (P)'].tolist()
volumes = df['Volume (V)'].tolist()
temperaturas = df['Temperatura (T)'].tolist()

tuplas = list(zip(pressoes, volumes, temperaturas))
tuplas = tuple(tuplas)
print(tuplas)