teste = ((10, 2, 5),(20, 1, 5), (20, 2, 10), (40, 1, 10), (10, 2, 5))
#Recebe os dados do input como uma tupla de tuplas (P, V, T)
from math import log
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
#Verifica o tipo de transformação e calcula delta U, delta S, W e Q para cada uma delas.
#Se nenhum input for igual, assume que é adiabática.
        UAB = (3/2) * ((PB * VB) - (PA * VA))
#Isotérmica:
        if TA == TB:
        #if PA * VA == PB * VB:(problemas com operações de float)
            WAB = PA * VA * log(VB / VA)
            SAB = ((PA * VA)/TA) * log(VB/VA)
#Isobárica:
        elif PA == PB:
            WAB = PA * (VB - VA)
            SAB = (5/2) * ((PA * VA)/TA) * log(TB/TA)
#Isocórica:
        elif VA == VB:
            WAB = 0
            SAB = (3/2) * ((PA * VA)/TA) * log(TB/TA) 
#Adiabática:
        else:
        #elif PA * (VA**(5/3)) == PB * (VB**(5/3)):(problemas com operações de float)
            WAB = -UAB
            SAB = 0
        QAB = WAB + UAB
        transformações.append((QAB, WAB, UAB, SAB))
#Lista Q, W e delta U de cada transformação em ordem, na forma de tuplas.
#Agora, calcula Qrecebido, Qcedido, W, delta U e delta S totais e rendimento e adiciona por último na lista.
# Depois transforma em tupla. Se não for um ciclo, o rendimento é None.
    Qr = 0
    Qc = 0
    W = 0
    U = 0
    S = 0
    for t in range(len(transformações)):
        if transformações[t][0] >= 0:
            Qr += transformações[t][0]
        else:
            Qc += transformações[t][0]
        W += transformações[t][1]
        U += transformações[t][2]
        S += transformações[t][3]
    if teste[0] == teste[-1]:
        rendimento = W/Qr
    else:
        rendimento = None
    total = (Qr,Qc, W, U, S, rendimento)
    transformações.append(total)
    transformações = tuple(transformações)
    return transformações
print(calculadora(teste))