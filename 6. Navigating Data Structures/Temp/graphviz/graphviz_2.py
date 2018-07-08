from graphviz import Graph
from math import floor

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
romania_location_map_full = {
    'Arad' : {'pos': (21.31227,46.18656), 'connections': ['Sibiu','Timisoara','Zerind'] },
    'Sibiu' : {'pos': (24.12558,45.79833), 'connections': ['Fagaras','Rimnicu Vilcea','Oradea'] },
    'Zerind' : {'pos': (21.51742,46.62251), 'connections': ['Oradea'] },
    'Timisoara' : {'pos': (21.20868,45.74887), 'connections': ['Lugoj'] },
    'Oradea' : {'pos': (21.91894,47.04650), 'connections': [] },
    'Fagaras' : {'pos': (24.97310,45.84164), 'connections': ['Bucharest'] },
    'Lugoj' : {'pos': (21.90346,45.69099), 'connections': ['Mehadia'] },
    'Rimnicu Vilcea' : {'pos': (24.36932,45.09968), 'connections': ['Craiova','Pitesti'] },
    'Mehadia' : {'pos': (22.36452,44.90411), 'connections': ['Dobreta'] },
    'Dobreta' : {'pos': (22.65973,44.63692), 'connections': ['Craiova'] },
    'Craiova' : {'pos': (23.79488,44.33018), 'connections': [] },
    'Pitesti' : {'pos': (24.86918,44.85648), 'connections': ['Bucharest','Craiova'] },
    'Bucharest' : {'pos': (26.10254,44.42677), 'connections': ['Giurgiu','Urziceni'] },
    'Giurgiu' : {'pos': (25.96993,43.90371), 'connections': [] },
    'Urziceni' : {'pos': (26.64112,44.71653), 'connections': ['Hirsova','Vaslui'] },
    'Vaslui' : {'pos': (27.72765,46.64069), 'connections': ['Lasi'] },
    'Lasi' : {'pos':(27.60144,47.15845), 'connections': ['Neamt'] },
    'Neamt' : {'pos': (26.38188,46.97587), 'connections': [] },
    'Hirsova' : {'pos': (27.94566,44.68935), 'connections': ['Eforie'] },
    'Eforie' : {'pos': (28.65273,44.04911), 'connections': [] }
}

# calculating geodesic SLDs
import geopy.distance
def calculate_GD(M, start, end):

    (x0,y0) = M[start]['pos']
    (x1,y1) = M[end]['pos']
    return floor(geopy.distance.geodesic((y0,x0), (y1,x1)).miles)


# GRAPHVIZ MODULE
G = Graph(format='png', engine='neato')
G.attr(overlap='compress')
G.attr(sep='3')
G.attr('edge', fontsize='9', color='grey', fontcolor='#7c7c7c')
G.attr('node', shape='box', width='0.1', height='0.1', style='filled', fontname="Arial", fontsize='10', fixedsize='true', color="#666666")

Map = romania_location_map_full
for node in Map.keys():
    (posX, posY) = Map[node]['pos']
    G.node(node, pos='{},{}!'.format(posX,posY), xlabel=node, label='')
for node in Map.keys():
    for con_node in Map[node]['connections']:
        G.edge(node, con_node, label=str(calculate_GD(Map, node, con_node)))

#print(G.source)


