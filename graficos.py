
import matplotlib.pyplot as plt
import numpy as np

def plotar_graficos(resultados):
    # Verifica se há pelo menos 2 pontos para uma transformação
    if len(resultados) < 2:
        print("São necessários pelo menos 2 pontos para uma transformação")
        return
    
    # Lista para armazenar as figuras
    figuras = []

    # Plota um gráfico para cada par de pontos consecutivos
    for i in range(len(resultados)-1):
        figuras.append(plt.figure(figsize=(8, 5)))  # Cria nova figura para cada transformação
        

        P1, V1, T1 = resultados[i]
        P2, V2, T2 = resultados[i+1]
        
        # Plota os pontos experimentais
        plt.plot([V1, V2], [P1, P2], 'ro', label='Dados experimentais')
        
        # Determina o tipo de transformação
        if P1 == P2:  # Isobárica
            plt.plot([V1, V2], [P1, P2], 'b-', label='Isobárica')
            plt.title(f'Transformação {i+1}: Isobárica')
        elif V1 == V2:  # Isocórica
            plt.plot([V1, V2], [P1, P2], 'g-', label='Isocórica')
            plt.title(f'Transformação {i+1}: Isocórica')
        elif T1 == T2:  # Isotérmica
            volumes = np.linspace(V1, V2, 100)
            pressoes = (8.314 * T1) / volumes  # Assumindo n=1 mol
            plt.plot(volumes, pressoes, 'm-', label=f'Isotérmica (T={T1} K)')
            plt.title(f'Transformação {i+1}: Isotérmica')
        else:  # Adiabática ou outra
            plt.plot([V1, V2], [P1, P2], 'k-', label='Transformação geral')
            plt.title(f'Transformação {i+1}: Geral')
        
        # Configurações comuns
        plt.xlabel('Volume (m³)')
        plt.ylabel('Pressão (Pa)')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
    for fig in reversed(figuras):
        fig.show()