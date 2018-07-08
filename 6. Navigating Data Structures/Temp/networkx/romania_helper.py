import networkx as nx 
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter,Line,Marker,Figure, Data, Layout, XAxis,YAxis
from plotly.offline import plot
from math import floor

"""
# Template to use
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
"""

# Build the graph
def load_map_graph(map_dict):
    G = nx.Graph()
    for node in map_dict.keys():
        G.add_node(node, pos=map_dict[node]['pos'])
    for node in map_dict.keys():
        for con_node in map_dict[node]['connections']:
            G.add_edge(node, con_node, length=10)
    return G

# calculating geodesic SLDs
import geopy.distance
def calculate_GD(G, start, end):

    (x0,y0) = G.node[start]['pos']
    (x1,y1) = G.node[end]['pos']
    return floor(geopy.distance.geodesic((y0,x0), (y1,x1)).miles)

#   PLOTTING USING PLOTLY
def show_map(G, start=None, goal=None, path=None, SLDTarget=None):
    # Reference: https://plot.ly/python/network-graphs/

    # Create Edges in plotly
    edge_trace = Scatter(
        x=[],
        y=[],   
        line=Line(width=0.5,color='#888'),
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
        textposition='right',
        mode='markers+text',
        hoverinfo='none',
        marker=Marker(
            opacity=0
        ),
        textfont=dict(color='blue')
    )

    node_trace = Scatter(
        x=[],
        y=[],
        text=[],
        textposition='top',
        textfont=dict(color='black'),
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
                titleside='right'
            ),
            line=dict(width=1)))

    node_SLD_trace = Scatter(
        x=[],
        y=[],
        text=[],
        textposition='bottom',
        textfont=dict(color='red'),
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
        color = '#0486ff'  #default
        if path and node in path:
            color = '#ff6404'
        if node == start:
            color = '#ff6404'
        elif node == goal:
            color = '#ff6404'        
        node_trace['marker']['color'].append(color)

    # Create network graph
    fig = Figure(data=Data([edge_trace, node_trace, edge_label_trace, node_SLD_trace]),
                layout=Layout(
                    title='<br>Romania Pathfinding Problem',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),               
                    xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

    plot(fig) #for python in command prompt


# test the library
# graph = load_map_graph(romania_location_map)
# show_map(graph,start='A',goal='B',path=['A','S','F','B'],SLDTarget='B')
#show_map(G)