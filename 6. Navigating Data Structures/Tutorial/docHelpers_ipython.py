"""
Purpose: A ipython helper file in the background to help visualization of search algorithms using networkx and graphviz libraries
Author: Parthiban Rajendran (parthi292929@gmail.com)
Date: 22nd May 2018
"""
from graphviz import Graph, Digraph, Source
from math import floor

from wand.image import Image as Image2 #to differentiate from ipython's image
from wand.api import library
from wand.color import Color

from operator import itemgetter
import base64 #for html conversion
import os, shutil #for temp render
import networkx as nx 
import pydot 

romania_location_map_open = {
    'A' : {'pos': (21.31227,46.18656), 'connections': ['S','T','Z'] },
    'S' : {'pos': (24.12558,45.79833), 'connections': ['F','RV'] },
    'Z' : {'pos': (21.51742,46.62251), 'connections': ['O'] },
    'T' : {'pos': (21.20868,45.74887), 'connections': ['LU'] },
    'O' : {'pos': (21.91894,47.04650), 'connections': [] },
    'F' : {'pos': (24.97310,45.84164), 'connections': ['B'] },
    'LU' : {'pos': (21.90346,45.69099), 'connections': ['M'] },
    'RV' : {'pos': (24.36932,45.09968), 'connections': ['C','P'] },
    'M' : {'pos': (22.36452,44.90411), 'connections': ['D'] },
    'D' : {'pos': (22.65973,44.63692), 'connections': [] },
    'C' : {'pos': (23.79488,44.33018), 'connections': [] },
    'P' : {'pos': (24.86918,44.85648), 'connections': [] },
    'B' : {'pos': (26.10254,44.42677), 'connections': ['G','U'] },
    'G' : {'pos': (25.96993,43.90371), 'connections': [] },
    'U' : {'pos': (26.64112,44.71653), 'connections': ['H','V'] },
    'V' : {'pos': (27.72765,46.64069), 'connections': ['LA'] },
    'LA' : {'pos':(27.60144,47.15845), 'connections': ['N'] },
    'N' : {'pos': (26.38188,46.97587), 'connections': [] },
    'H' : {'pos': (27.94566,44.68935), 'connections': ['E'] },
    'E' : {'pos': (28.65273,44.04911), 'connections': [] }
}

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

romania_location_map_open_full = {
    'Arad' : {'pos': (21.31227,46.18656), 'connections': ['Sibiu','Timisoara','Zerind'] },
    'Sibiu' : {'pos': (24.12558,45.79833), 'connections': ['Fagaras','Rimnicu Vilcea'] },
    'Zerind' : {'pos': (21.51742,46.62251), 'connections': ['Oradea'] },
    'Timisoara' : {'pos': (21.20868,45.74887), 'connections': ['Lugoj'] },
    'Oradea' : {'pos': (21.91894,47.04650), 'connections': [] },
    'Fagaras' : {'pos': (24.97310,45.84164), 'connections': ['Bucharest'] },
    'Lugoj' : {'pos': (21.90346,45.69099), 'connections': ['Mehadia'] },
    'Rimnicu Vilcea' : {'pos': (24.36932,45.09968), 'connections': ['Craiova','Pitesti'] },
    'Mehadia' : {'pos': (22.36452,44.90411), 'connections': ['Dobreta'] },
    'Dobreta' : {'pos': (22.65973,44.63692), 'connections': [] },
    'Craiova' : {'pos': (23.79488,44.33018), 'connections': [] },
    'Pitesti' : {'pos': (24.86918,44.85648), 'connections': [] },
    'Bucharest' : {'pos': (26.10254,44.42677), 'connections': ['Giurgiu','Urziceni'] },
    'Giurgiu' : {'pos': (25.96993,43.90371), 'connections': [] },
    'Urziceni' : {'pos': (26.64112,44.71653), 'connections': ['Hirsova','Vaslui'] },
    'Vaslui' : {'pos': (27.72765,46.64069), 'connections': ['Lasi'] },
    'Lasi' : {'pos':(27.60144,47.15845), 'connections': ['Neamt'] },
    'Neamt' : {'pos': (26.38188,46.97587), 'connections': [] },
    'Hirsova' : {'pos': (27.94566,44.68935), 'connections': ['Eforie'] },
    'Eforie' : {'pos': (28.65273,44.04911), 'connections': [] }
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

def initializeMap(Map):
    # GRAPHVIZ MODULE
    G = Graph(format='png', engine='neato', strict=True)
    G.attr(overlap='compress')
    G.attr(sep='3')
    G.attr('edge', fontsize='9', color='#e0e1e2', fontcolor='#1f4cef')
    G.attr('node', shape='circle', width='0.15', height='0.1', style='filled', fontname="Arial", fontsize='9', fixedsize='true', color="#666666")

    #Map = romania_location_map
    for node in Map.keys():
        (posX, posY) = Map[node]['pos']
        #node = node + '\n366'
        G.node(node, pos='{},{}!'.format(posX,posY), xlabel=node, label="")
    for node in Map.keys():
        for con_node in Map[node]['connections']:
            G.edge(node, con_node, label=str(calculate_GD(Map, node, con_node)))

    return G

def initializeTree():
    # Tree map in networkx
    X = nx.Graph() 
    return X

def initializeDataStructure():
    # DATA STRUCTURES.. QUEUE OR STACK..
    data_dot = Digraph(format='png')
    data_dot.attr('node', shape='record', width='0.4')

    return data_dot


class Doc:
    def __init__(self,Map):
        self._map_dot = initializeMap(Map)
        self._tree_dot = initializeTree()
        self._data_dot = initializeDataStructure()

        #for computing
        self.data_dot_last = []     #earlier child nodes needed for data_dot caz we redraw entirely every time called   

        #for rendering/saving
        self._map_dot_frames = []
        self._tree_dot_frames = []
        self._data_dot_frames = []

        #for temp render
        self.baseFolder = 'docs/'
        shutil.rmtree(self.baseFolder + 'images', ignore_errors=True)   

        #for tracking progress (experimental) 
        self.cameFrom = { }
           
    def showMap(self,highlightList=None):
        """
        Returns the raw map blob for ipython to just display it
        """
        if highlightList:
            for eachHighLightNode in highlightList:
                self._map_dot.node(eachHighLightNode, color='black', fillcolor='orange')

        return self._map_dot.pipe()
    
    def computeGraphs(self,baseNode=None,childNodes=None,mappy=True,tree=False,queue=False,HTML=False):
        """
        1. Highlights map with active baseNode and childNodes and returns the updated map
        2. Also creates/updates corresponding current queue/stack and tree structure and returns them as well
        3. By default, sends mappy
        """
        if baseNode is None and childNodes is None:
            raise ValueError('One or both arguments missing')

        # MAP 
        self._map_dot.node(baseNode, color='black', fillcolor='green')
        node = baseNode
        while self.cameFrom.get(node,None) is not None:
            self._map_dot.edge(node, self.cameFrom[node], color='red')
            node = self.cameFrom[node]
        for eachChild in childNodes:
            self._map_dot.node(eachChild, color='black', fillcolor='orange')           


        # TREE
        highlight_node_attr = {'fillcolor':'green','shape':'circle','width':'0.4','style':'filled','fixedsize':'true'}
        highlight_edge_attr = {'fillcolor':'#eabc77','shape':'circle','width':'0.4','style':'filled','fixedsize':'true'}
        X = self._tree_dot
        X.add_node(baseNode, **highlight_node_attr)
        for eachChild in childNodes:
            X.add_node(eachChild, **highlight_edge_attr)
            X.add_edge(baseNode, eachChild)
        treeG = self.nxToDot(X)


        # DATA STRUCTURE/CONTAINER LIKE Q, STACK, PRIO Q, ETC
        if baseNode in self.data_dot_last: self.data_dot_last.remove(baseNode)       
        for eachChild in childNodes:        
            self.data_dot_last.append(eachChild)
            self.cameFrom[eachChild] = baseNode
        j=0
        temp_list = []
        for eachChild in self.data_dot_last:
            temp_list.append('<f' + str(j) + '> ' + eachChild)
            j += 1
        data_label = '|'.join(temp_list)
        self._data_dot = initializeDataStructure()
        self._data_dot.node('current', label=baseNode, style='filled', fillcolor='green')
        self._data_dot.attr(rankdir='RL')
        topChild = str(0)
        self._data_dot.edge('queue' + ':f'+ topChild, 'current')
        self._data_dot.node('queue', label='{ '+ data_label +' }', style='filled', fillcolor='yellow')


        #packaging
        map_dot_output = self._map_dot.pipe()
        tree_dot_output = treeG.pipe()
        data_dot_output = self._data_dot.pipe()

        #store frames for rendering anim gif later
        self._map_dot_frames.append(map_dot_output)
        self._tree_dot_frames.append(tree_dot_output)
        self._data_dot_frames.append(data_dot_output)

        #return the pipe output to avoid saving to files..     
        returnList = []
        if mappy is True:
            returnList.append(self._map_dot.pipe())    
        if tree is True:
            returnList.append(treeG.pipe())    
        if queue is True:
            returnList.append(self._data_dot.pipe()) 

        if HTML is True:
            return self.stack3ImagesHTML(returnList)

        return returnList               

    def render(self):
        tree_dot_blob = self.renderWand(self._tree_dot_frames)
        data_dot_blob = self.renderWand(self._data_dot_frames)
        map_dot_blob = self.renderWand(self._map_dot_frames)
        #tree_data_combined_blob = self.stack2Images(data_dot_blob,tree_dot_blob)
        return data_dot_blob, tree_dot_blob, map_dot_blob #,tree_data_combined_blob

    # Below is adapted method with workaround as suggested in link below
    # https://stackoverflow.com/questions/50387437/frames-not-disappearing-in-python-wand/
    def renderWand(self, dot_frames):
        
        wand = Image2()        

        #get max frame height, width
        frameSizeList = []
        tempImgList = []
        for each_frame in dot_frames:
            img = Image2(blob=each_frame)
            frameSizeList.append((img.width,img.height))
            #print('image width: {} height: {}'.format(img.width,img.height))
            tempImgList.append(img)
        optimalWidth = (max(frameSizeList,key=itemgetter(0)))[0]
        optimalHeight = (max(frameSizeList,key=itemgetter(1)))[1]
        #print('Max Frame size detected: ',optimalFrameSize)

        #create frames
        for each_frame in tempImgList:
            newImg = Image2(width=optimalWidth, height=optimalHeight, background=Color('WHITE'))
            newImg.composite(each_frame,0,0)
            wand.sequence.append(newImg)

        #set frame rate
        for cursor in range(len(tempImgList)):
            with wand.sequence[cursor] as frame:
                #print('sequence width: {} height: {}'.format(frame.width,frame.height))
                frame.delay = 100

        #wand.merge_layers('merge')
        wand.format = 'gif'
        wand.save(filename='animated.gif')
        #print('No of frames: {} gif width: {} height: {}'.format(len(wand.sequence),wand.width,wand.height))
        blob = wand.make_blob()
        wand.close()

        return blob

    def stack3ImagesHTML(self, returnList):

        if not returnList:
            raise ValueError('Argument missing for stack3ImagesHTML')

        template = """
            <div><img src="data:image/png;base64, {image}" alt="Red dot"/></div>
            """            
        images_html = ''
        for each_blob in reversed(returnList):  #reversed is just a preference of images order
            _ = template
            _ = _.format(image=base64.b64encode(each_blob).decode('utf-8'))
            images_html += _   

        HTML =  '<div style="display:flex;" >' +  images_html + '</div>'    

        return HTML


    def updateParent(self, child, newParent):
        """
        This is useful, when cameFrom is updated in algorithm, and has to reflect in our 
        visualization. For eg, tentative gScore in A Star
        """
        oldParent = self.cameFrom.get(child,None)

        if oldParent is not None:
            self.cameFrom[child] = newParent

            self._tree_dot.remove_edge(oldParent,child)
            self._tree_dot.remove_node(child)

            baseNode = newParent
            childNodes = [child]  
            highlight_node_attr = {'fillcolor':'green','shape':'circle','width':'0.4','style':'filled','fixedsize':'true'}
            highlight_edge_attr = {'fillcolor':'#eabc77','shape':'circle','width':'0.4','style':'filled','fixedsize':'true'}
            self._tree_dot.add_node(baseNode, **highlight_node_attr)
            for eachChild in childNodes:
                self._tree_dot.add_node(eachChild, **highlight_edge_attr)
                self._tree_dot.add_edge(baseNode, eachChild)
            
        

    def nxToDot(self, X):
        """
        return networkx in Dot format typically for rendering
        """
        P = nx.nx_pydot.to_pydot(X)   
        M = Source(P, engine='dot',format='png')
        return M

# mainly to get neighbors..
def getNetworkxGraph(Map):
    nG = nx.Graph()
    for node in Map.keys():
        nG.add_node(node, pos=Map[node]['pos'])
    for node in Map.keys():
        for con_node in Map[node]['connections']:
            nG.add_edge(node, con_node, length=str(calculate_GD(Map, node, con_node)))   

    return nG


