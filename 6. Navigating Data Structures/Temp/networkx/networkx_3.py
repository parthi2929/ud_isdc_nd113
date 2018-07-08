import networkx as nx 
import pydot
from graphviz import Source, render

romania_location_map = {
    'A' : {'pos': (21.31227,46.18656), 'connections': ['S','T','Z'] },
    'S' : {'pos': (24.12558,45.79833), 'connections': ['F','RV','O'] },
    'Z' : {'pos': (21.51742,46.62251), 'connections': ['O'] },
    'T' : {'pos': (21.20868,45.74887), 'connections': ['LU'] },
    'O' : {'pos': (21.91894,47.04650), 'connections': [] },
    'F' : {'pos': (24.97310,45.84164), 'connections': ['B'] },
    'LU' : {'pos': (21.90346,45.69099), 'connections': ['M'] },
    'RV' : {'pos': (24.36932,45.09968), 'connections': ['C','P'] },
    'M' : {'pos': (22.36452,44.90411), 'connections': ['D'] },
    'D' : {'pos': (22.65973,44.63692), 'connections': ['C'] },
    'C' : {'pos': (23.79488,44.33018), 'connections': [] },
    'P' : {'pos': (24.86918,44.85648), 'connections': ['B','C'] },
    'B' : {'pos': (26.10254,44.42677), 'connections': ['G','U'] },
    'G' : {'pos': (25.96993,43.90371), 'connections': [] },
    'U' : {'pos': (26.64112,44.71653), 'connections': ['H','V'] },
    'V' : {'pos': (27.72765,46.64069), 'connections': ['LA'] },
    'LA' : {'pos':(27.60144,47.15845), 'connections': ['N'] },
    'N' : {'pos': (26.38188,46.97587), 'connections': [] },
    'H' : {'pos': (27.94566,44.68935), 'connections': ['E'] },
    'E' : {'pos': (28.65273,44.04911), 'connections': [] }
}

# NETWORKX MODULE
G = nx.Graph()
Map = romania_location_map
for node in Map.keys():
    G.add_node(node, pos=Map[node]['pos'])
for node in Map.keys():
    for con_node in Map[node]['connections']:
        G.add_edge(node, con_node, length=10)


#  NETWORX TO PYDOT TO GRAPHVIZ MODULE
P = nx.nx_pydot.to_pydot(G)

# before sending to neato, fix the pos values
# 1. A [pos="(21.31227, 46.18656)"]; should become A [pos="21.31227, 46.18656!"];
P1 = str(P).replace('"(', '"').replace(')"','!"')
print(P1)
M = Source(P1, engine='neato',format='png')

# NOT WORKING START #-------------------
# M.attr(overlap='compress')
# M.attr(sep='3')
# M.attr('edge', fontsize='9', color='grey', fontcolor='#7c7c7c')
# M.attr('node', shape='box', width='0.1', height='0.1', style='filled', fontname="Arial", fontsize='10', fixedsize='true', color="#666666")
# NOT WORKING END #---------------------

M.render('test1', view=True)  
