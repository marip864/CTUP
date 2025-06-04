import pandas as pd

pressao = float(input())
volume = float(input())
temperatura = float(input())
def salvar_arquivo(pressao, volume, temperatura):
    # Cria um DataFrame com os dados
    df = pd.DataFrame({
        'Pressão (P)': [pressao],
        'Volume (V)': [volume],
        'Temperatura (T)': [temperatura]
    })
    
    # Salva o DataFrame em um arquivo CSV
    df.to_csv('dados_termodinamicos.csv', index=False)
    print("Dados salvos no arquivo 'dados_termodinamicos.csv'.")

teste = salvar_arquivo(pressao, volume, temperatura)
print(teste)