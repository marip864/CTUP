import matplotlib.pyplot as plt
def grafico_de_dados(x, y, titulo='Gráfico de Dados', xlabel='Eixo X', ylabel='Eixo Y'):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title(teste)
    plt.xlabel(eixo x)
    plt.ylabel(eixo y)
    plt.grid(True)
    plt.show() 