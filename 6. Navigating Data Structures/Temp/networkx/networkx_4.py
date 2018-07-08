from graphviz import Digraph, Source, render
import networkx as nx 
import pydot


"""
Aim: Removing edge in a graphviz is not possible directly. So
1. Create a networkx graph
2. Render as Graphviz
3. Change the networkx graph
4. Render again as Graphviz
"""

# 1. Create a networkx graph
def createNx():

    G = nx.Graph()

    baseNode = 'A'
    childNodes = ['S','T','Z']

    G.add_node(baseNode, fillcolor='green')
    for eachChild in childNodes:
        G.add_edge(baseNode, eachChild)

    baseNode = 'S'
    childNodes = ['O','RV','F']    

    G.add_node(baseNode)
    for eachChild in childNodes:
        G.add_edge(baseNode, eachChild)

    baseNode = 'F'
    childNodes = ['B']    

    G.add_node(baseNode)
    for eachChild in childNodes:
        G.add_edge(baseNode, eachChild)    

    baseNode = 'RV'
    childNodes = ['C','P']    

    G.add_node(baseNode)
    for eachChild in childNodes:
        G.add_edge(baseNode, eachChild)      

    return G

treeX = createNx()      
print("Nodes: {} Edges: {}".format( treeX.number_of_nodes(), treeX.number_of_edges() ))
    
# 2.  Render as Graphviz
def nxToDot(G):

    #  NETWORX TO PYDOT TO GRAPHVIZ MODULE
    P = nx.nx_pydot.to_pydot(G)
    print(P)
    return P

nxToDot(treeX)
    
# 3. Change the networkx graph
def changeEdgeNx(G, oldParent, newParent, childNode):

    G.remove_edge(oldParent, childNode)
    G.add_edge(newParent, childNode)

changeEdgeNx(treeX, 'F', 'P', 'B')
nxToDot(treeX)