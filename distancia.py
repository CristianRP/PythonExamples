import math
def distancia(x1, x2, y1, y2):
    distancia = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    print(distancia)

distancia(2,3,4,2)