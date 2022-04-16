import ast
from lib2to3.pgen2 import token
from matplotlib.font_manager import json_dump
import numpy as np
from api.app.petriNets.graph import graf
import json


def construction(data):
    places = list((data['places']).keys())
    tokens = list((data)['places'].values())
    transitions = list((data)['transitions'])
    input = (data)['input']
    output = (data)['output']
    mOutPut = indicenceMatrixOutPut(input, places, transitions)
    mInPut = indicenceMatrixInPut(output, places, transitions)
    mIndicence = indicenceMatrix(mInPut, mOutPut)
    arratshooting = shootings(transitions, data['shooting'])
    newState = statusChange(tokens,mIndicence,arratshooting)
    graf(places,transitions,mOutPut,mInPut,newState)
    return newState

# a+
def indicenceMatrixInPut(input, places, transition):
    matrixOutout = np.zeros((np.size(transition), np.size(places)))
    # print(input['t1'])
    for i in range(np.size(transition)):
        try:
            x = transition[i]
            for j in input[x]:
                k = places.index(j)
                matrixOutout[(i, k)] = 1
        except:
            print("no está")
    return(matrixOutout)


# a-
def indicenceMatrixOutPut(input, places, transition):
    matrixInput = np.zeros((np.size(transition), np.size(places)))
    # print(input['t1'])
    for i in range(np.size(transition)):
        try:
            x = transition[i]
            for j in input[x]:
                k = places.index(j)
                matrixInput[(i, k)] = 1
        except:
            print("no está")
    return(matrixInput)


def indicenceMatrix(mInPut, mOutPut):
    matrix = mInPut - mOutPut
    return matrix


def shootings(transitions, shootingData):
    arrayShooting = np.zeros(np.size(transitions))

    for i in shootingData:
        arrayShooting[transitions.index(i)] += 1

    return(arrayShooting)


def statusChange(tokens, mIndicence, arratshooting):
    newStatus = tokens + np.dot(arratshooting,mIndicence)
    return newStatus

def validationFormat():
    pass




    
def Analytics(places,tokens,transitions,input,output,shooting):
    arrayPlaces = AnalyticsTexts(places)
    arrayTokens = list(np.array(AnalyticsTexts(tokens), dtype = 'float'))
    arrayTransitions = AnalyticsTexts(transitions)
    arrayShooting = AnalyticsTexts(shooting)
    arrayInput = AnalyticsTextsComple(input)
    arrayOutPut = AnalyticsTextsComple(output)
    mOutPut = indicenceMatrixOutPut(arrayInput, arrayPlaces, arrayTransitions)
    mInPut = indicenceMatrixInPut(arrayOutPut, arrayPlaces, arrayTransitions)
    mIndicence = indicenceMatrix(mInPut, mOutPut)
    arratshooting = shootings(arrayTransitions, arrayShooting)
    newState = statusChange(arrayTokens,mIndicence,arratshooting)
    return graf(arrayPlaces,arrayTransitions,mOutPut,mInPut,newState)
    


def AnalyticsTexts(places):
    arrayPlaces = []
    places = places.replace(" ", "")
    for i in range(len(places)):
        if(places[i] == ','):
            ini = i
            end = places.find(',',ini+1)
            cad =places[slice(int(ini+1),int(end))]
            arrayPlaces.append(cad)
    arrayPlaces.pop()
    return arrayPlaces

def AnalyticsAux(places):
    arrayPlaces = []
    places = places.replace(" ", "")
    for i in range(len(places)):
        if(places[i] == '-'):
            ini = i
            end = places.find('-',ini+1)
            cad =places[slice(int(ini+1),int(end))]
            arrayPlaces.append(cad)
    arrayPlaces.pop()
    return arrayPlaces

def AnalyticsTextsComple(places):
    arrayTransition = []
    arrayPlaces = []
    places = places.replace(" ", "")
    for i in range(len(places)):
        if(places[i] == ','):
            ini = i
            end = places.find('(',ini+1)
            cad =places[slice(int(ini+1),int(end))]
            arrayTransition.append(cad)

    arrayTransition.pop()
    index = 0
    diccionary = dict()
    for i in range(len(places)):
            if(places[i] == '('):
                ini = i
                end = places.find(')',ini+1)
                arrayPlaces = AnalyticsAux(places[slice(int(ini+1),int(end))])
                diccionary [arrayTransition[index]] = arrayPlaces
                index+=1
    return diccionary







