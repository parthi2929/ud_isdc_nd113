#https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search

# graph is in adjacent list representation
graph = {
        'A': ['S', 'T', 'Z'],
        'S': ['F', 'RV'],
        'T': ['LU'],
        'Z': ['O'],
        'F': ['B'],
        'B': ['G','U'],
        'U':['V','H'],
        'V':['LA'],
        'LA':['N'],
        'RV':['C','P'],
        'LU':['M'],
        'M':['D'],
        'E':['H']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    i = 0
    while queue:
        
        i = i + 1
        print("Step: {} Node: {}   open: {}".format(i,queue[0][-1],queue))

        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]

        
        # path found
        if node == end:
            return path
        
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
            #print("Node: {} New Path: {}".format(node,new_path))

print(bfs(graph, 'A', 'B'))