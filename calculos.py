teste = ((10, 2, 5),(20, 1, 5), (20, 2, 10), (40, 1, 10), (10, 2, 5))
from math import log
def calculadora(tupla):
    for n in range(len(tupla)):
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
        WAB = PA * VA * log(VB / VA)
    elif PA == PB:
        WAB = PA * (VB - VA) 
    elif VA == VB:
        WAB = 0 
    else:
        WAB = -UAB