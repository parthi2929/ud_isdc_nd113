# Program to print BFS traversal from a given source
# vertex. BFS(int s) traverses vertices reachable
# from s.
from collections import defaultdict
 
# This class represents a directed graph using adjacency
# list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        # visited = [False]*(len(self.graph))
        visited = defaultdict(bool) #because node could be of any label, not just integer
 
        # Create a frontier for BFS
        frontier = []
 
        # Mark the source node as visited and enfrontier it
        frontier.append(s)
        visited[s] = True
 
        # if frontier is empty, quit 
        while frontier:
 
            # Defrontier a vertex from frontier and print it
            s = frontier.pop(0)
            print(s)
 
            # Get all adjacent vertices of the defrontierd
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enfrontier it
            for i in self.graph[s]:
                if visited[i] == False:
                    frontier.append(i)
                    visited[i] = True
 
 
# Driver code
# Create a graph given in the above diagram
g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'C')
g.addEdge('C', 'A')
g.addEdge('C', 'D')
g.addEdge('D', 'D')
 
print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS('C')