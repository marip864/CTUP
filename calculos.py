teste = ((10, 2, 5),(20, 1, 5), (20, 2, 10), (40, 1, 10), (10, 2, 5))
#Recebe os dados do input como uma tupla de tuplas (P, V, T)
from math import log
def calculadora(tupla):
    transformações = [] #Aqui ficam os valores reais, para aproximar no final
    transformações_arredondadas = [] #Aqui ficam os valores aproximados
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
#Se nenhum input for igual, assume que é adiabática reversível.
        UAB = (3/2) * ((PB * VB) - (PA * VA))
#Isotérmica:
        if TA == TB:
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
            WAB = -UAB
            SAB = 0
        QAB = WAB + UAB
#Lista Q, W e delta U de cada transformação em ordem, na forma de tuplas, e arredonda.
        transformações.append((QAB, WAB, UAB, SAB))
        transformações_arredondadas.append((round(QAB,3), round(WAB,3), round(UAB, 3), round(SAB, 3)))
#Agora, calcula Qrecebido, Qcedido, Q, W, delta U e delta S totais, arredonda e adiciona por último.
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
        Q = Qr + Qc
        W += transformações[t][1]
        U += transformações[t][2]
        S += transformações[t][3]
    total_arredondado = (round(Qr,3),round(Qc,3),round(Q,3), round(W,3),round(U,3),round(S,3))
    transformações_arredondadas.append(total_arredondado)
#Se for um ciclo, calcula o rendimento aproximado.
    if teste[0] == teste[-1]:
        rendimento = W/Qr
        transformações_arredondadas.append(round(rendimento, 3))
#Agora transforma os dados na tupla a ser retornada.
    transformações_arredondadas = tuple(transformações_arredondadas)
    return transformações_arredondadas
print(calculadora(teste))