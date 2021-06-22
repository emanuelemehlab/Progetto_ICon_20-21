import re
import numpy as np
from pyswip import Prolog
import os

def spaceCheck(nomeCitta):  #controlla la presenza di spazi e soostituisco
    if ' ' in nomeCitta:
        nomeCitta=nomeCitta.replace(" ","_")

    return nomeCitta

def getCityName(): #ottenere una lista contenente tutti i nomi delle città nella Kb
    city=list()
    prolog=Prolog()
    prolog.consult("PrologFile/CityKB.pl")
    query="city(Namecity,Continent,State,Fo)."
    for cityDict in prolog.query(query):
        city.append(cityDict["Namecity"])

    return city

def getLocationName(cityName): #ottenere le location di una data città
    location = list()
    prolog = Prolog()
    prolog.consult("PrologFile/CityKB.pl")
    query = "showplace("+cityName+", Nome , Categoria , Giorni , Orario , Prezzo ,Nodo)."
    for locationDict in prolog.query(query):
        location.append(locationDict["Nome"])

    return location

def getStationName(cityName): #ottenere tutte le stazioni di una città
    station = list()
    prolog = Prolog()
    prolog.consult("PrologFile/CityKB.pl")
    query = "station("+cityName+",Nome,Nodo)."
    for stationDict in prolog.query(query):
        station.append(stationDict["Nome"])

    return station

def FileName(strCityName):

    if strCityName=="tokyo":
        return "Tokyo"
    elif strCityName=="londra":
        return "Londra"
    elif strCityName=="amsterdam":
        return "Amsterdam"
    elif strCityName=="san_paolo":
        return "San Paolo"
    elif strCityName=="parigi":
        return "Parigi"
    elif strCityName=="new_york":
        return  "New York"
    elif strCityName=="berlino":
        return "Berlino"
    elif strCityName=="buenos_aires":
        return "Buenos Aires"
    elif strCityName=="istanbul":
        return "Istanbul"
    elif strCityName=="madrid":
        return "Madrid"
    elif strCityName=="mosca":
        return "Mosca"
    else:
        return "NULL"

def deleteImg():

    if os.path.exists("GraphImage1.png"):
        os.remove("GraphImage1.png")
        #plt.savefig("GraphImage.png", format="png")


def isNumber(number):
    if number.isAlpha:
        return False
    else:
        return True

