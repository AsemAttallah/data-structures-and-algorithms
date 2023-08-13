from collections import deque

class Queue:
    def __init__(self):
        self.dq=deque()
    def enqueue(self):
        self.dq.append()
    def dequeue(self):
        self.dq.popleft()

class Vertix:
    def __init__(self, value):
        self.value=value

class Edge:
    def __init__(self,vertix,weight=0):
        self.vertix=vertix
        self.weight=weight

class Graph:
    def __init__(self):
        self.__adj_list={}

    def add_vertix(self,value):
        '''
        Argument:value
        Return: The added vertix 
        Add a vertix to the graph
        '''
        vertix=Vertix(value)
        self.__adj_list[vertix]=[]
        return vertix
    
    def add_edge(self,start_vertix,end_vertix,weight=0):
        '''
        Arguments: 2 vertices to be connected by the edge,weight(optional)
        Return: None
        Adds a new edge between two vertices in the graph
        if specified, assign a weight to the edge 
        Both vertices should already be in the graph
        '''
        edge1 = Edge(end_vertix)
        edge2 = Edge(start_vertix)

        if start_vertix not in self.__adj_list:
            raise KeyError(" vertix not exist")
        if end_vertix not in self.__adj_list:
            raise KeyError(" vertix not exist")

        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)
    
    def get_vertices(self):
        '''
        Argument: None
        Return: all of the vertices in the graph as a 
        collection (set, list, or similar)
        Empty collection returned if there are no vertices
        '''
        return self.__adj_list.keys()
    
    def size(self):
        '''
        Argument: None
        Return: The total number of vertices in the graph
        '''
        return len(self.__adj_list)
    
    def get_neighbors(self,vertix):
        '''
        Argument: vertix
        Return a collection of edge connected to the 
        given vertix
        Include the weight of the connection in the returned collection 
        Empty collection returned if there are no vertices
        '''
        return self.__adj_list.get(vertix, [])