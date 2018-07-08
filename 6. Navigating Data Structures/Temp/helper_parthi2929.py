"""
This helper is a modified version of helpers.py used in Udacity iSDC "Implement Route planner"
This has been initially created to create romania map but could also be used for any graph
that is compliant with template graphs given below. 
"""

import networkx as nx 
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter,Line,Marker,Figure, Data, Layout, XAxis,YAxis
from plotly.offline import iplot,init_notebook_mode
from math import floor,sqrt,pow


init_notebook_mode(connected=True)



# Template to use
romania_location_map = {
    'A' : {'pos': (21.31227,46.18656), 'connections': ['S','T','Z'] },
    'S' : {'pos': (24.12558,45.79833), 'connections': ['F','RV','O'] },
    'Z' : {'pos': (21.51742,46.62251), 'connections': ['O'] },
    'T' : {'pos': (21.20868,45.74887), 'connections': ['LU'] },
    'F' : {'pos': (24.97310,45.84164), 'connections': ['B'] },
    'LU' : {'pos': (21.90346,45.69099), 'connections': ['M'] },
    'RV' : {'pos': (24.36932,45.09968), 'connections': ['C','P'] },
    'M' : {'pos': (22.36452,44.90411), 'connections': ['D'] },
    'D' : {'pos': (22.65973,44.63692), 'connections': ['C'] },
    'P' : {'pos': (24.86918,44.85648), 'connections': ['B','C'] },
    'B' : {'pos': (26.10254,44.42677), 'connections': ['G','U'] },
    'U' : {'pos': (26.64112,44.71653), 'connections': ['H','V'] },
    'V' : {'pos': (27.72765,46.64069), 'connections': ['LA'] },
    'LA' : {'pos':(27.60144,47.15845), 'connections': ['N'] },
    'H' : {'pos': (27.94566,44.68935), 'connections': ['E'] },
    
    #'C' and 'O' are not really dead ended, but connection not included solely caz already included earlier
    # current algo starting here may have problem
    'C' : {'pos': (23.79488,44.33018), 'connections': [] },    
    'O' : {'pos': (21.91894,47.04650), 'connections': [] },        
    
    # these guys are dead ended but you can go backwards
    # currently algo starting here may have problem
    'N' : {'pos': (26.38188,46.97587), 'connections': [] },    
    'G' : {'pos': (25.96993,43.90371), 'connections': [] },    
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
map_40_dict = {
	0: {'pos': (0.7801603911549438, 0.49474860768712914), 'connections': [36, 34, 31, 28, 17]}, 
	1: {'pos': (0.5249831588690298, 0.14953665513987202), 'connections': [35, 31, 27, 26, 25, 20, 18, 17, 15, 6]}, 
	2: {'pos': (0.8085335344099086, 0.7696330846542071), 'connections': [39, 36, 21, 19, 9, 7, 4]}, 
	3: {'pos': (0.2599134798656856, 0.14485659826020547), 'connections': [35, 20, 15, 11, 6]}, 
	4: {'pos': (0.7353838928272886, 0.8089961609345658), 'connections': [39, 36, 21, 19, 9, 7, 2]}, 
	5: {'pos': (0.09088671576431506, 0.7222846879290787), 'connections': [32, 16, 14]}, 
	6: {'pos': (0.313999018186756, 0.01876171413125327), 'connections': [35, 20, 15, 11, 1, 3]}, 
	7: {'pos': (0.6824813442515916, 0.8016111783687677), 'connections': [39, 36, 22, 21, 19, 9, 2, 4]}, 
	8: {'pos': (0.20128789391122526, 0.43196344222361227), 'connections': [33, 30, 14]}, 
	9: {'pos': (0.8551947714242674, 0.9011339078096633), 'connections': [36, 21, 19, 2, 4, 7]}, 
	10: {'pos': (0.7581736589784409, 0.24026772497187532), 'connections': [31, 27, 26, 25, 24, 18, 17, 13]}, 
	11: {'pos': (0.25311953895059136, 0.10321622277398101), 'connections': [35, 20, 15, 3, 6]}, 
	12: {'pos': (0.4813859169876731, 0.5006237737207431), 'connections': [37, 34, 31, 28, 22, 17]}, 
	13: {'pos': (0.9112422509614865, 0.1839028760606296), 'connections': [27, 24, 18, 10]}, 
	14: {'pos': (0.04580558670435442, 0.5886703168399895), 'connections': [33, 30, 16, 5, 8]}, 
	15: {'pos': (0.4582523173083307, 0.1735506267461867), 'connections': [35, 31, 26, 25, 20, 17, 1, 3, 6, 11]}, 
	16: {'pos': (0.12939557977525573, 0.690016328140396), 'connections': [37, 30, 5, 14]}, 
	17: {'pos': (0.607698913404794, 0.362322730884702), 'connections': [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15]}, 
	18: {'pos': (0.719569201584275, 0.13985272363426526), 'connections': [31, 27, 26, 25, 24, 1, 10, 13, 17]}, 
	19: {'pos': (0.8860336256842246, 0.891868301175821), 'connections': [21, 2, 4, 7, 9]}, 
	20: {'pos': (0.4238357358399233, 0.026771817842421997), 'connections': [35, 26, 1, 3, 6, 11, 15]}, 
	21: {'pos': (0.8252497121120052, 0.9532681441921305), 'connections': [2, 4, 7, 9, 19]}, 
	22: {'pos': (0.47415009287034726, 0.7353428557575755), 'connections': [39, 37, 29, 7, 12]}, 
	23: {'pos': (0.26253385360950576, 0.9768234503830939), 'connections': [38, 32, 29]}, 
	24: {'pos': (0.9363713903322148, 0.13022993020357043), 'connections': [27, 10, 13, 18]}, 
	25: {'pos': (0.6243437191127235, 0.21665962402659544), 'connections': [34, 31, 27, 26, 1, 10, 15, 17, 18]}, 
	26: {'pos': (0.5572917679006295, 0.2083567880838434), 'connections': [34, 31, 27, 1, 10, 15, 17, 18, 20, 25]}, 
	27: {'pos': (0.7482655725962591, 0.12631654071213483), 'connections': [31, 1, 10, 13, 18, 24, 25, 26]}, 
	28: {'pos': (0.6435799740880603, 0.5488515965193208), 'connections': [39, 36, 34, 31, 0, 12, 17]}, 
	29: {'pos': (0.34509802713919313, 0.8800306496459869), 'connections': [38, 37, 32, 22, 23]}, 
	30: {'pos': (0.021423673670808885, 0.4666482714834408), 'connections': [33, 8, 14, 16]}, 
	31: {'pos': (0.640952694324525, 0.3232711412508066), 'connections': [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28]}, 
	32: {'pos': (0.17440205342790494, 0.9528527425842739), 'connections': [38, 5, 23, 29]}, 
	33: {'pos': (0.1332965908314021, 0.3996510641743197), 'connections': [8, 14, 30]}, 
	34: {'pos': (0.583993110207876, 0.42704536740474663), 'connections': [0, 12, 17, 25, 26, 28, 31]}, 
	35: {'pos': (0.3073865727705063, 0.09186645974288632), 'connections': [1, 3, 6, 11, 15, 20]}, 
	36: {'pos': (0.740625863119245, 0.68128520136847), 'connections': [39, 0, 2, 4, 7, 9, 28]}, 
	37: {'pos': (0.3345284735051981, 0.6569436279895382), 'connections': [12, 16, 22, 29]}, 
	38: {'pos': (0.17972981733780147, 0.999395685828547), 'connections': [23, 29, 32]}, 
	39: {'pos': (0.6315322816286787, 0.7311657634689946), 'connections': [2, 4, 7, 22, 28, 36]}
}

class Map:
	def __init__(self, G):
		self._graph = G
		self.intersections = nx.get_node_attributes(G, "pos")
		self.roads = [list(G[node]) for node in G.nodes()]

def load_map_40(map_40_dict):
	G = load_map_graph(map_40_dict)
	return Map(G)

# Build the graph
def load_map_graph(map_dict):
    G = nx.Graph()
    for node in map_dict.keys():
        G.add_node(node, pos=map_dict[node]['pos'])
    for node in map_dict.keys():
        for con_node in map_dict[node]['connections']:
            G.add_edge(node, con_node)
    return G

# calculating geodesic SLDs
import geopy.distance
def calculate_GD(G, start, end):

    (x0,y0) = G.node[start]['pos']
    (x1,y1) = G.node[end]['pos']
    return floor(geopy.distance.geodesic((y0,x0), (y1,x1)).miles)

#  PLOTTING USING PLOTLY
def show_map_improved(M, start=None, goal=None, path=None, SLDTarget=None):
    G = M._graph
    show_map(G, start, goal, path, SLDTarget)

def show_map(G, start=None, goal=None, path=None, SLDTarget=None):
    # Reference: https://plot.ly/python/network-graphs/
    # print(goal)
    # Create Edges in plotly
    edge_trace = Scatter(
        x=[],
        y=[],   
        line=Line(width=0.5,color='#BDBDBD'),
        hoverinfo='none',
        mode='lines+text',
        text= []
        )

    # invisible nodes for edge labels..
    # courtesy: https://stackoverflow.com/questions/46037897/line-hover-text-in-plotly
    edge_label_trace = Scatter(
        x=[],
        y=[],
        text=[],
        textposition='top',
        mode='markers+text',
        hoverinfo='none',
        marker=Marker(
            opacity=0
        ),
        textfont=dict(size=9, color='blue')
    )

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        textposition='left',
        textfont=dict(size=10, color='black'),
        mode='markers+text',
        hoverinfo='none',
        marker=Marker(
            showscale=False,
            colorscale='Hot',
            reversescale=True,
            color=[],
            size=15,
            colorbar=dict(
                thickness=5,
                title='Node Connections',
                xanchor='left',
                titleside='left'
            ),
            line=dict(width=0)))

    node_SLD_trace = Scatter(
        x=[],
        y=[],
        text=[],
        textposition='top',
        textfont=dict(size=9,color='red'),
        mode='markers+text',
        hoverinfo='none',
        marker=Marker(size=15,opacity=0),
        line=dict(width=1))

    for edge in G.edges():
        text = calculate_GD(G, edge[1],edge[0])    # NODE DISTANCE CALCULATED HERE
        x0, y0 = G.node[edge[0]]['pos']
        x1, y1 = G.node[edge[1]]['pos']    
        edge_trace['x'] += [x0, x1, None]
        edge_trace['y'] += [y0, y1, None]  

        #invisible node at middle of edges to place edge labels
        edge_label_trace['x'].append((x0+x1)/2)
        edge_label_trace['y'].append((y0+y1)/2)
        edge_label_trace['text'].append(text)
        
    for node in G.nodes():
        text = node
        x, y = G.node[node]['pos']
        node_trace['x'].append(x)
        node_trace['y'].append(y)
        node_trace['text'].append(text)

    for node in G.nodes():
        if not SLDTarget is None:
            text = calculate_GD(G, node,SLDTarget) 
            x, y = G.node[node]['pos']
            node_SLD_trace['x'].append(x)
            node_SLD_trace['y'].append(y)
            node_SLD_trace['text'].append(text)

    # Color Node Points in plotly
    for node in G.nodes():
        color = '#1976D2'  #default
        if path and node in path:
            color = '#FF5252'
        if node == start:
            color = '#FF5252'
        elif node == goal:
            color = '#FF5252'  
        node_trace['marker']['color'].append(color)

    # Create network graph
    fig = Figure(data=Data([edge_trace, node_trace, edge_label_trace, node_SLD_trace]),
                layout=Layout(
                    autosize=True,
                    title='<br>Plotted using Plotly',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),               
                    #xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False, constrain='domain'),
                    #yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False, scaleanchor='x'),
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False),                    
                    ))


    iplot(fig) #for python in command prompt


# test the library
# graph = load_map_graph(romania_location_map)
# show_map(graph,start='A',goal='B',path=['A','S','F','B'],SLDTarget='B')
#show_map(G)