import math
def calculoEntreDoisPontos(x1,y1,x2,y2):
    if x1==x2: #Linha reta na vertical
        distancia = y2-y1
    if y1==y2: #Linha reta na horizontal
        distancia = x2 - x1
    else:
        distancia = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return distancia
x1, y1 , x2, y2 = float(input("x1:")), float(input("y1:")), float(input("x2:")), float(input("y2:"))
distanciaEntreDoisPontos = calculoEntreDoisPontos(x1,y1,x2,y2)
print(f"{distanciaEntreDoisPontos:.2f}")