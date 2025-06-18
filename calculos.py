#Recebe os dados do input como uma tupla (PA, VA, TA, PB, VB, TB)
from math import log
def calculadora(PA, VA, TA, PB, VB, TB):
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
#Lista Q, W e delta U em ordem, na forma de tuplas, e arredonda.
        transformações = ((round(QAB,3), round(WAB,3), round(UAB, 3), round(SAB, 3)))
        return transformações