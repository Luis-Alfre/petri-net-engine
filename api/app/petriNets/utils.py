from lib2to3.pgen2 import token
import numpy as np


def construction(data):
    places = list((data['places']).keys())
    tokens = list((data)['places'].values())
    transitions = list((data)['transitions'])
    input = (data)['input']
    output = (data)['output']
    print(input)
    mOutPut = indicenceMatrixOutPut(input, places, transitions)
    mInPut = indicenceMatrixInPut(output, places, transitions)
    print(mInPut)
    print(mOutPut)
    mIndicence = indicenceMatrix(mInPut, mOutPut)
    print(mIndicence)

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
    matriz = mInPut - mOutPut
    return matriz
