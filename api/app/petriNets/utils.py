from lib2to3.pgen2 import token
import numpy as np
from api.app.petriNets.graph import graf


def construction(data):
    places = list((data['places']).keys())
    tokens = list((data)['places'].values())
    transitions = list((data)['transitions'])
    input = (data)['input']
    output = (data)['output']
    mOutPut = indicenceMatrixOutPut(input, places, transitions)
    mInPut = indicenceMatrixInPut(output, places, transitions)
    mIndicence = indicenceMatrix(mInPut, mOutPut)
    arratshooting = shooting(transitions, data['shooting'])
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


def shooting(transitions, shootingData):
    arrayShooting = np.zeros(np.size(transitions))

    for i in shootingData:
        arrayShooting[transitions.index(i)] += 1

    return(arrayShooting)


def statusChange(tokens, mIndicence, arratshooting):
    newStatus = tokens + np.dot(arratshooting,mIndicence)
    return newStatus

def validationFormat():
    pass
