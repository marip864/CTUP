
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
        
        # Determina o tipo de transformação
        if P1 == P2:  # Isobárica
            if round(V1 / T1) != round(V2 / T2):  # Verifica se é uma isobárica válida
                # Criar um "X" com preenchimento
                theta = np.linspace(0, 2*np.pi, 100)
                x1 = 0.5 + 0.3 * np.cos(theta + np.pi/4)  # Primeira perna do X
                x2 = 0.5 + 0.3 * np.cos(theta - np.pi/4)  # Segunda perna do X
                plt.fill(x1, x2, color='red', alpha=0.5)
                plt.text(0.5, 0.5, "X", fontsize=100, ha='center', va='center', color='darkred')
                plt.plot(label="Erro", color='darkred')
                plt.title(f'Transformação {i+1}: Erro! Seus valores não satisfazem a lei de Charles')
            else:
                plt.plot([V1, V2], [P1, P2], 'o', label='Dados experimentais', color = "cornflowerblue")
                plt.plot([V1, V2], [P1, P2], '-', label='Isobárica', color = "deeppink")
                plt.title(f'Transformação {i+1}: Isobárica')
        elif V1 == V2:  # Isocórica
            if round(P1 / T1) != round(P2 / T2):  # Verifica se é uma isocórica válida
                # Criar um "X" com preenchimento
                theta = np.linspace(0, 2*np.pi, 100)
                x1 = 0.5 + 0.3 * np.cos(theta + np.pi/4)  # Primeira perna do X
                x2 = 0.5 + 0.3 * np.cos(theta - np.pi/4)  # Segunda perna do X
                plt.fill(x1, x2, color='red', alpha=0.5)
                plt.text(0.5, 0.5, "X", fontsize=100, ha='center', va='center', color='darkred')
                plt.plot(label="Erro", color='darkred')
                plt.title(f'Transformação {i+1}: Erro! Seus valores não satisfazem a lei de Gay-Lussac')
            else:
                plt.plot([V1, V2], [P1, P2], 'o', label='Dados experimentais', color = "royalblue")
                plt.plot([V1, V2], [P1, P2], '-', label='Isocórica', color = "lightseagreen")
                plt.title(f'Transformação {i+1}: Isocórica')
        elif T1 == T2:  # Isotérmica
            if round(P1 * V1) != round(P2 * V2):  # Verifica se é uma isotérmica válida
                # Criar um "X" com preenchimento
                theta = np.linspace(0, 2*np.pi, 100)
                x1 = 0.5 + 0.3 * np.cos(theta + np.pi/4)  # Primeira perna do X
                x2 = 0.5 + 0.3 * np.cos(theta - np.pi/4)  # Segunda perna do X
                plt.fill(x1, x2, color='red', alpha=0.5)
                plt.text(0.5, 0.5, "X", fontsize=100, ha='center', va='center', color='darkred')
                plt.plot(label="Erro", color='darkred')
                plt.title(f'Transformação {i+1}: Erro! Seus valores não satisfazem a lei de Boyle')
            else:
                plt.plot([V1, V2], [P1, P2], 'o', label='Dados experimentais', color = "deeppink") # Plota os pontos experimentais
                volumes = np.linspace(V1, V2, 100) # Fornece volumes para a curva teórica
                razao = (P1 * V1) / T1
                pressoes = (razao * T1) / volumes # Calcula as pressões teóricas
                plt.plot(volumes, pressoes, '-', label=f'Isotérmica (T={T1} K)', color = "darkorange")
                plt.title(f'Transformação {i+1}: Isotérmica')
        else:  # Adiabática ou outra
            # Criar um "X" com preenchimento
            theta = np.linspace(0, 2*np.pi, 100)
            x1 = 0.5 + 0.3 * np.cos(theta + np.pi/4)  # Primeira perna do X
            x2 = 0.5 + 0.3 * np.cos(theta - np.pi/4)  # Segunda perna do X
            plt.fill(x1, x2, color='red', alpha=0.5)
            plt.text(0.5, 0.5, "X", fontsize=100, ha='center', va='center', color='darkred')
            plt.plot(label="Erro", color='darkred')
            plt.title(f'Transformação {i+1}: Erro! A CTUP não serve a esse propósito')
        
        # Configurações comuns
        plt.xlabel('Volume (m³)')
        plt.ylabel('Pressão (Pa)')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
    for fig in reversed(figuras):
        fig.show()