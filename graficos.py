
import matplotlib.pyplot as plt
import numpy as np

def plotar_graficos(resultados):
    P = [ponto[0] for ponto in resultados]
    V = [ponto[1] for ponto in resultados]
    T = [ponto[2] for ponto in resultados]
    plt.plot(V, P, 'ro', label='Dados experimentais')  # Pontos vermelhos
    if len(resultados) == 2:
        if resultados[0][0] == resultados[1][0]:  # Isobárica
            plt.plot(V, P, 'b-')  # Linha azul conectando os pontos
            plt.xlabel('Volume (m³)')
            plt.ylabel('Pressão (Pa)')
            plt.title('Gráfico Isobárico')

        elif resultados[0][1] == resultados[1][1]:  # Isocórica
            plt.plot(V, P, 'b-')  # Linha azul conectando os pontos
            plt.xlabel('Volume (m³)')
            plt.ylabel('Pressão (Pa)')
            plt.title('Gráfico Isocórico')

        elif resultados[0][2] == resultados[1][2]:  # Isotérmica
            T = resultados[0][2]  # Temperatura constante
            
            # Criando uma faixa de volumes para uma curva suave
            volumes = np.linspace(min(V), max(V), 100)
            
            # Constantes
            R = 8.314  # Constante dos gases (J/(mol*K))
            n = 1       # Número de moles (assumido)
            
            # Calculando a pressão usando P = nRT/V
            pressoes = (n * R * T) / volumes
            
            # O código precisa plotar a curva teórica para que o python consiga plotar o gráfico com umas curva
            plt.plot(volumes, pressoes, 'b-', label=f'Curva isotérmica (T = {T} K)')
            
            plt.xlabel('Volume (m³)')
            plt.ylabel('Pressão (Pa)')
            plt.title('Gráfico Isotérmico')
            plt.legend()


        else:
            plt.plot(V, P, 'b-')  # Linha azul conectando os pontos
            plt.xlabel('Volume (m³)')
            plt.ylabel('Pressão (Pa)')
            plt.title('Gráfico Adiabática')


    elif len(resultados) == 3:
        if all(t == T[0] for t in T):  # Isotérmica
            v_curve = np.linspace(min(V), max(V), 100)
            p_curve = (8.314 * T[0]) / v_curve
            plt.plot(v_curve, p_curve, 'b-', label=f'Isotérmica (T={T[0]} K)')
            
        elif all(p == P[0] for p in P):  # Isobárica
            plt.hlines(P[0], min(V), max(V), colors='b', linestyles='-', 
                      label=f'Isobárica (P={P[0]} Pa)')
            
        elif all(v == V[0] for v in V):  # Isocórica
            plt.vlines(V[0], min(P), max(P), colors='b', linestyles='-',
                     label=f'Isocórica (V={V[0]} m³)')
            
        else:  # Transformação composta (ex: isocórica + isotérmica)
            # Plota linhas conectando os pontos
            plt.plot(V, P, 'b--', alpha=0.5, label='Transformação composta')
    
    # Configurações comuns
    plt.xlabel('Volume (m³)')
    plt.ylabel('Pressão (Pa)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()  # Mostra UMA única figura


# Testando com seus dados
dados_isobarica = (
    (101325, 0.0224, 300),  # Pressão (Pa), Volume (m³), Temperatura (K)
    (101325, 0.0448, 600)   # Pressão mantida constante
)
dados_isocorica = (
    (101325, 0.0224, 300),  # Pressão (Pa), Volume (m³), Temperatura (K)
    (202650, 0.0224, 600)   # Volume mantido constante
)
dados_isotermica = (
    (101325, 0.0224, 273.15),  # Pressão (Pa), Volume (m³), Temperatura (K)
    (202650, 0.0112, 273.15)   # Temperatura mantida constante (Lei de Boyle: P ∝ 1/V)
)
dados_adiabatica = (
    (101325, 0.0224, 300),  # Pressão (Pa), Volume (m³), Temperatura (K)
    (202650, 0.0150, 400)   # Nenhuma das variáveis é constante
)
dados_tres_pontos = (
        (101325, 0.02, 300),   # Ponto 1 (início isocórica)
        (202650, 0.02, 600),   # Ponto 2 (fim isocórica/início isotérmica)
        (101325, 0.04, 600)    # Ponto 3 (fim isotérmica)
)
plotar_graficos(dados_isobarica)   # Deve identificar como isobárica
plotar_graficos(dados_isocorica)   # Deve identificar como isocórica
plotar_graficos(dados_isotermica)  # Deve identificar como isotérmica
plotar_graficos(dados_adiabatica)  # Deve identificar como adiabática
plotar_graficos(dados_tres_pontos)