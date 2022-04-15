import numpy as np

from graphviz import Digraph

def graf(places, transitions, mOutput, mInput, tokens):

    f = Digraph('TrafficLights', filename='fsm', format='png')

    for i in transitions:
        f.attr('node', shape='box')
        f.node(i,label=i.upper())

    for i in range(np.size(places)):
      f.attr('node', shape='circle')
      f.node(places[i],label=str(tokens[i]))  

    for i in range(len(mOutput[0])):
        print(len(mOutput))
        print(len(mOutput[0]))
        for j in range(len(mOutput)):
            if mOutput[j][i] != 0:
               f.edge(places[i],transitions[j])
            if mInput[j][i] != 0:
                f.edge(transitions[j],places[i])

    f.view()