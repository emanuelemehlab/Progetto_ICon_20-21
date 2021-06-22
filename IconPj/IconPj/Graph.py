import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import numpy as np
from pyswip import Prolog
import GeneralFunction as gf


pos = {1: (0, 1),
           2: (0, 6),
           3: (-1, 4),
           4: (-1, -4),
           5: (1, 4),
           6: (1, -4),
           7: (2, 5.65),
           8: (2, -5.65),
           9: (-2, 5.65),
           10: (-2, -5.65),
           11: (0, 3),
           12: (3, 0),
           13: (0, -1),
           14: (0, -3),
           15: (-3, 0),
           16: (4, 4.47),
           17: (4, -4.47),
           18: (-4, -4.47),
           19: (-4, 4.47),
           20: (5.50, 2.80),
           21: (5.50, -2.80),
           22: (-5.50, 2.80),
           23: (-5.50, -2.80),
           24: (6, 0),
           25: (-6, 0),
           26: (0, -6),
           27: (2, 2),
           28: (-2, 2),
           29: (2, -2),
           30: (-2, -2)
           }

#-----------------------------------------------------------------------------------
#funzione che clcola la distanza euclidea tra due punti
def euclideanDistance(source, goal):  #funzione che clcola la distanza euclidea tra due punti
    x1, y1 = pos.get(source)
    x2, y2 = pos.get(goal)
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#-------------------------------------------------------------------------------------

def SearchPath(start,arrival,nameFile):
    g = nx.Graph()
    nameFile=gf.FileName(nameFile)
    gf.deleteImg()

    with open("C:/Users/Pronto all'uso/PycharmProjects/IconProject/CityFile/"+nameFile+".txt", "r") as f:
        number_lines = f.readline()
        i = 1
        while i <= int(number_lines):
            f_content = f.readline()
            # print(i,f_content)
            a = np.array(f_content.split(","))
            g.add_edge(int(a[0]), int(a[1]), weight=float(a[2]))
            i = i + 1
            #print(a[2])
        f.close()

    prolog = Prolog()
    prolog.consult("PrologFile/CityKB.pl")

    city=gf.spaceCheck(str(nameFile).lower())
    if start in gf.getStationName(city):
        strStart = "station(" + city + "," + start + ",Node)."  # costruzione delle query
    else:
        strStart = "showplace(" + city + "," + start + " , Categoria , Giorni , Orario , Prezzo , Node )."

    if arrival in gf.getStationName(city):
        strArrival = "station(" + city + "," + arrival + ",Node)."  # costruzione delle query

    else:
        strArrival = "showplace(" + city + "," + arrival + " , Categoria , Giorni , Orario , Prezzo , Node )."


    startNode=1
    arrivalNode=1
    for startNodeDict in prolog.query(strStart):  # query per il punto di partenza
        startNode = int(startNodeDict["Node"])

    for arrivalNodeDict in prolog.query(strArrival):  # query per l'arrivo
        arrivalNode = int(arrivalNodeDict["Node"])


    shortestPath = nx.astar_path(g, startNode, arrivalNode, heuristic=euclideanDistance)

    x = 0
    totalSumPath = 0
    while x < len(shortestPath):
        if x == (len(shortestPath) - 1):
            break
        a = g.get_edge_data(shortestPath[x], shortestPath[x + 1]).pop('weight')
        totalSumPath = totalSumPath + a
        x = x + 1


    return (round(totalSumPath, 2) * 10) , shortestPath

