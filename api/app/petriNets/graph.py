# import networkx as nx
# import matplotlib.pyplot as plt
import numpy as np
# def graf():
#     g = nx.DiGraph('finite_state_machine')
#     g.add_nodes_from([1,2,3,4,5])
#     g.add_nodes_from([10,11],color="red")
#     g.add_edge(1,2, color='green' )
#     g.add_edge(4,2)
#     g.add_edge(3,5)
#     g.add_edge(2,3)
#     g.add_edge(5,4)

#     nx.draw(g,with_labels=True)
#     plt.draw()
#     plt.savefig("./api/app")


from graphviz import Digraph

def graf(places, transitions, mOutput, mInput, tokens):

    f = Digraph('TrafficLights', filename='fsm', format='png')

    for i in transitions:
        f.attr('node', shape='box')
        f.node(i,label=i.upper())

    for i in range(np.size(places)):
      f.attr('node', shape='circle')
      f.node(places[i],label=str(tokens[i]))  

    for i in range(len(mOutput)):
        for j in range(len(mOutput[0])):
    

    # f.attr('node', shape='circle')
    # f.node('p1',label='P1')
    # f.node('p2',label='P2')


    # f.edge('p1','t1')
    # f.edge('p2', 't1')
    # f.edge('t2', 'p2')
 


    f.view()