import matplotlib.pyplot as plt
from math import log
dados = ((101325, 0.0224, 273.15),(202650, 0.0112, 273.15), (303975, 0.0082, 350.15), 
         (101325, 0.0245, 298.15), (101325, 0.0224, 273.15))
def calculadora(tupla):
    transformações = []
    for n in range(len(tupla)-1):
        pontoA = tupla[n]
        pontoB = tupla[n+1]
        PA = pontoA[0]
        VA = pontoA[1]
        TA = pontoA[2]
        PB = pontoB[0]
        VB = pontoB[1]
        TB = pontoB[2]
        UAB = (3/2) * ((PB * VB) - (PA * VA))
        if TA == TB:
        #if PA * VA == PB * VB:(problemas com operações de float)
            WAB = PA * VA * log(VB / VA)
#Isobárica:
        elif PA == PB:
            WAB = PA * (VB - VA)
#Isocórica:
        elif VA == VB:
            WAB = 0 
#Adiabática:
        else:
        #elif PA * (VA**(5/3)) == PB * (VB**(5/3)):(problemas com operações de float)
            WAB = -UAB
        QAB = WAB + UAB
        transformações.append((QAB, WAB, UAB))
#Lista Q, W e delta U de cada transformação em ordem, na forma de tuplas.
#Agora, calcula Q, W e delta U totais e adiciona por último na lista. Depois a transforma em tupla.
    Q = 0
    W = 0
    U = 0
    for t in range(len(transformações)):
        Q += transformações[t][0]
        W += transformações[t][1]
        U += transformações[t][2]
    total = (Q, W, U)
    transformações.append(total)
    transformações = tuple(transformações)
    return transformações

print(calculadora(dados))
    
resultados = ((-1573.2222927732964, -1573.2222927732964, 0.0),
               (0.0, -334.3725000000006, 334.3725000000006), 
               (0.0, 15.198750000000246, -15.198750000000246), 
               (-531.9562500000005, -212.7825000000001, -319.1737500000004), 
               (-2105.178542773297, -2105.178542773297, 0.0))


P = [pressao[0] / 1000 for pressao in resultados]
V = [volume[1] for volume in resultados]

plt.figure(figsize=(10, 6))
plt.plot(V, P, marker='o', linestyle='-', color='b', linewidth=2)
plt.title("Ciclo Termodinâmico - Pressão vs Volume", fontsize=14)
plt.xlabel("Volume (m³)", fontsize=12)
plt.ylabel("Pressão (kPa)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

for i, (v, p) in enumerate(zip(V, P)):
    plt.annotate(f'Ponto {i+1}\n({v:.4f} m³, {p:.2f} kPa)', 
                 (v, p), 
                 textcoords="offset points", 
                 xytext=(10,5), 
                 ha='left')
plot = plt.show()
