from helpers import Map, load_map_10, load_map_40, show_map 
import math 

# Do not change this cell
# When you write your methods correctly this cell will execute
# without problems
class PathPlanner():
    """Construct a PathPlanner Object"""
    def __init__(self, M, start=None, goal=None):
        """ """
        self.map = M
        self.start= start
        self.goal = goal
        self.closedSet = self.create_closedSet() if goal != None and start != None else None
        self.openSet = self.create_openSet() if goal != None and start != None else None
        self.cameFrom = self.create_cameFrom() if goal != None and start != None else None
        #self.gScore = self.create_gScore() if goal != None and start != None else None
        #self.fScore = self.create_fScore() if goal != None and start != None else None
        self.path = self.run_search() if self.map and self.start != None and self.goal != None else None
        
    def get_path(self):
        """ Reconstructs path after search """
        if self.path:
            return self.path 
        else :
            self.run_search()
            return self.path
    
    def reconstruct_path(self, current):
        """ Reconstructs path after search """
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path[:-1]
    
    def add_to_openSet(self, neighbor):     
        """
        Adding to priority Q, both a neighbor n and total cost f(n) involved in arriving at that neighbor
        total cost f(n) is stored as priority        
        """
        fScore = self.create_fScore(neighbor)
        self.openSet.put( (fScore, neighbor) )    

    def run_search(self):
        """ """
        if self.map == None:
            raise ValueError("Must create map before running search. Try running PathPlanner.set_map(start_node)")
        if self.goal == None:
            raise ValueError("Must create goal node before running search. Try running PathPlanner.set_goal(start_node)")
        if self.start == None:
            raise ValueError("Must create start node before running search. Try running PathPlanner.set_start(start_node)")

        self.closedSet = self.closedSet if self.closedSet != None else self.create_closedSet()
        self.openSet = self.openSet if self.openSet != None else  self.create_openSet()
        self.cameFrom = self.cameFrom if self.cameFrom != None else  self.create_cameFrom()
        #self.gScore = self.gScore if self.gScore != None else  self.create_gScore()
        #self.fScore = self.fScore if self.fScore != None else  self.create_fScore()

        while not self.is_open_empty():
            
            cost, current = self.get_current_node()

            if (current == self.goal):
                self.path = [x for x in reversed(self.reconstruct_path(current))]
                return self.path
            
            else:
                #self.openSet.remove(current) not necessary as its a Queue
                self.closedSet.add(current)
                
                for neighbor in self.get_neighbors(current):                             
                
                    if neighbor in self.closedSet:                                                                          
                        if (self.get_tenative_gScore(current, neighbor) >= self.get_gScore(neighbor)):                            
                            continue #to next iteration in for loop                                
                    self.record_best_path_to(current, neighbor)                     
                
                    if not neighbor in self.closedSet:                                                                    
                        self.add_to_openSet(neighbor)                         
                        self.closedSet.add(neighbor)  
        print("No Path Found")
        self.path = None
        return False

def create_closedSet(self):
    """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
    # TODO: return a data structure suitable to hold the set of nodes already evaluated
    return set()

from queue import PriorityQueue
def create_openSet(self):
    """ Creates and returns a data structure suitable to hold the set of currently discovered nodes 
    that are not evaluated yet. Initially, only the start node is known."""
    if self.start != None:
        openSet = PriorityQueue()           
        openSet.put((0,self.start))               
        return openSet
    
    raise ValueError("Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")

def create_cameFrom(self):
    """Creates and returns a data structure that shows which node can most efficiently be reached from another,
    for each node."""
    cameFrom = {}
    if self.start != None:
        cameFrom[self.start] = None
        return cameFrom
    raise ValueError("Must create start node before creating a cameFrom list. Try running PathPlanner.set_start(start_node)")            

def create_gScore(self, node):
    """Creates and returns a data structure that holds the cost of getting from the start node to that node, for each node.
    The cost of going from start to start is zero."""
    cost = 0
    if self.cameFrom.get(node) is None: return 0
    while True:   #when current_node is not None..        
        cost += self.distance(self.cameFrom.get(node),node)
        node = self.cameFrom.get(node)
        if self.cameFrom.get(node) is None: break
    return cost        

def create_fScore(self, neighbor):
    """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
    by passing by that node, for each node. That value is partly known, partly heuristic.
    For the first node, that value is completely heuristic."""
    # TODO:  a data structure that holds the total cost of getting from the start node to the goal
    # by passing by that node, for each node. That value is partly known, partly heuristic.
    # For the first node, that value is completely heuristic. The rest of the node's value should be 
    # set to infinity
    gScore = self.get_gScore(neighbor)  
    hScore = self.heuristic_cost_estimate(neighbor)  
    return gScore + hScore  

def _reset(self):
    """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
    self.closedSet = None
    self.openSet = None
    self.cameFrom = None
    self.gScore = None
    self.fScore = None
    self.path = self.run_search() if self.map and self.start and self.goal else None

def set_map(self, M):
    """Method used to set map attribute """
    self._reset(self)
    self.start = None
    self.goal = None
    # TODO: Set map to new value. 
    self.map = M 

def set_start(self, start):
    """Method used to set start attribute """
    self._reset(self)
    # TODO: Set start value. Remember to remove goal, closedSet, openSet, cameFrom, gScore, fScore, 
    # and path attributes' values.
    self._reset()
    self.start= start      
    
def set_goal(self, goal):
    """Method used to set goal attribute """
    self._reset(self)
    # TODO: Set goal value. 
    self.goal= goal

def get_current_node(self):
    """ Returns the node in the open set with the lowest value of f(node)."""
    # TODO: Return the node in the open set with the lowest value of f(node).
    return self.openSet.get()

def get_neighbors(self, node):
    """Returns the neighbors of a node"""
    # TODO: Return the neighbors of a node
    return self.map._graph.neighbors(node)

def get_gScore(self, node):
    """Returns the g Score of a node"""
    # TODO: Return the g Score of a node
    return self.create_gScore(node)

def get_tenative_gScore(self, current, neighbor):
    """Returns the tenative g Score of a node"""
    # TODO: Return the tenative g Score of the current node 
    # plus distance from the current node to it's neighbors
    return self.distance(current,neighbor) + self.create_gScore(current) 

def is_open_empty(self):
    """returns True if the open set is empty. False otherwise. """
    # TODO: Return True if the open set is empty. False otherwise.
    return self.openSet.empty() 

#!pip install geopy
import geopy.distance
from math import floor
def distance(self, node_1, node_2):
    """ Computes the Euclidean L2 Distance"""
    # TODO: Compute and return the Euclidean L2 Distance
    #print('distance start:{} end:{}'.format(node_1, node_2))
    (x0,y0) = self.map._graph.node[node_1]['pos']     
    (x1,y1) = self.map._graph.node[node_2]['pos']      
    return floor(geopy.distance.geodesic((y0,x0), (y1,x1)).miles)     

def heuristic_cost_estimate(self, node):
    """ Returns the heuristic cost estimate of a node """
    # TODO: Return the heuristic cost estimate of a node
    return self.distance(node, self.goal)

def calculate_fscore(self, neighbor):
    """Calculate the f score of a node. """
    # TODO: Calculate and returns the f score of a node. 
    # REMEMBER F = G + H   
    gScore = self.get_gScore(neighbor)  
    hScore = self.heuristic_cost_estimate(neighbor)  
    return gScore + hScore       
    
def record_best_path_to(self, current, neighbor):
    """Record the best path to a node """
    # TODO: Record the best path to a node, by updating cameFrom, gScore, and fScore
    self.cameFrom[neighbor] = current 

PathPlanner.create_closedSet = create_closedSet
PathPlanner.create_openSet = create_openSet
PathPlanner.create_cameFrom = create_cameFrom
PathPlanner.create_gScore = create_gScore
PathPlanner.create_fScore = create_fScore
PathPlanner._reset = _reset
PathPlanner.set_map = set_map
PathPlanner.set_start = set_start
PathPlanner.set_goal = set_goal
PathPlanner.get_current_node = get_current_node
PathPlanner.get_neighbors = get_neighbors
PathPlanner.get_gScore = get_gScore
PathPlanner.get_tenative_gScore = get_tenative_gScore
PathPlanner.is_open_empty = is_open_empty
PathPlanner.distance = distance
PathPlanner.heuristic_cost_estimate = heuristic_cost_estimate
PathPlanner.calculate_fscore = calculate_fscore
PathPlanner.record_best_path_to = record_best_path_to

map_40 = load_map_40()

planner = PathPlanner(map_40, 5, 34)
path = planner.path
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)