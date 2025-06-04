teste = ((10, 2, 5),(20, 1, 5), (20, 2, 10), (40, 1, 10), (10, 2, 5))
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
        UAB = (3/2) * ((PB * VB) - (PA * VA))
        #if TA == TB:
        if PA * VA == PB * VB:
            WAB = PA * VA * log(VB / VA)
        elif PA == PB:
            WAB = PA * (VB - VA) 
        elif VA == VB:
            WAB = 0 
        #else:
        elif PA * (VA**(5/3)) == PB * (VB**(5/3)):
            WAB = -UAB
        QAB = WAB + UAB
        transformações.append((QAB, WAB, UAB))
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
#print(calculadora(teste))