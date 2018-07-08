import networkx as nx 

map_10_dict = {
	0: {'pos': (0.7798606835438107, 0.6922727646627362), 'connections': [7, 6, 5]}, 
	1: {'pos': (0.7647837074641568, 0.3252670836724646), 'connections': [4, 3, 2]}, 
	2: {'pos': (0.7155217893995438, 0.20026498027300055), 'connections': [4, 3, 1]}, 
	3: {'pos': (0.7076566826610747, 0.3278339270610988), 'connections': [5, 4, 1, 2]}, 
	4: {'pos': (0.8325506249953353, 0.02310946309985762), 'connections': [1, 2, 3]}, 
	5: {'pos': (0.49016747075266875, 0.5464878695400415), 'connections': [7, 0, 3]}, 
	6: {'pos': (0.8820353070895344, 0.6791919587749445), 'connections': [0]}, 
	7: {'pos': (0.46247219371675075, 0.6258061621642713), 'connections': [0, 5]}, 
	8: {'pos': (0.11622158839385677, 0.11236327488812581), 'connections': [9]}, 
	9: {'pos': (0.1285377678230034, 0.3285840695698353), 'connections': [8]}
}



G = nx.Graph()

#Adding a node
G.add_node(1)

#Add list of nodes
G.add_nodes_from([2,3])

#edges
G.add_edge(1,2)

print("Nodes: {} Edges: {}".format( G.number_of_nodes(), G.number_of_edges() ))
G.clear()

for node in map_10_dict.keys():
    G.add_node(node, pos=map_10_dict[node]['pos'])
for node in map_10_dict.keys():
    for con_node in map_10_dict[node]['connections']:
        G.add_edge(node, con_node)
print("Nodes: {} Edges: {}".format( G.number_of_nodes(), G.number_of_edges() ))



