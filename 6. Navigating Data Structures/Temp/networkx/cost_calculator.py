import networkx as nx 
import matplotlib.pyplot as plt
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

# for edge weights..
import geopy.distance
def calculate_GD(M, start, end):
    (x0,y0) = M[start]['pos']
    (x1,y1) = M[end]['pos']
    return floor(geopy.distance.geodesic((y0,x0), (y1,x1)).miles)

# calculated total actual distance of connected nodes
def calculate_TAD(G, path): 
    """
    To implement
    """
    return None

# CONSTRUCT GRAPH       
G = nx.Graph()
Map = romania_location_map
for node in Map.keys():
    G.add_node(node, pos=Map[node]['pos'])
for node in Map.keys():
    for con_node in Map[node]['connections']:
        G.add_edge(node, con_node, length=calculate_GD(Map,node, con_node))

