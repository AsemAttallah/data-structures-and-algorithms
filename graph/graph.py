from collections import deque

class Queue:
    def __init__(self):
        self.dq=deque()
    def enqueue(self,value):
        self.dq.append(value)
    def dequeue(self):
        return self.dq.popleft()
    def __len__(self):
        return len(self.dq)

class Vertix:
    def __init__(self, value):
        self.value=value

class Edge:
    def __init__(self,vertix,weight=0):
        self.vertix=vertix
        self.weight=weight
    def __str__(self):
        return f"Edge to: {self.vertix.value}, Weight: {self.weight}"

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
    
    def get_all_neighbors(self):
        '''
        Argument: None
        Return all collection of edges 
        Get all neighbors in the graph
        '''
        egdes=""
        all_value= list(self.__adj_list.values())
        for values in all_value:
            for value in values:
                egdes+=value.__str__()+","
        return egdes
            
    def get_all_vertices_with_edges(self):
        '''
        Argument: None
        Return all collection of vertices and edges 
        Get all vertices and edges  in the graph
        '''
        all_vertices_edges="{"
        all_vertices=list(self.__adj_list.keys())
        all_egdes= list(self.__adj_list.values())

        for i in range(len(all_egdes)):
            all_vertices_edges+="|"+all_vertices[i].value+","
            for j in range(len(all_egdes[i])):
                all_vertices_edges+=all_egdes[i][j].__str__()+","
        return all_vertices_edges+"}"

    def breadth_first(self,start_vertix):
        q=Queue()
        result=[]
        visited=set()

        q.enqueue(start_vertix)
        visited.add(start_vertix)
        while len(q):
            current_vertix=q.dequeue()
            result.append(current_vertix.value)
            neighbors= self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor=edge.vertix
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)
        return result
    

if __name__=="__main__":
    g=Graph()
    a=g.add_vertix('A')
    # edge1 = Edge(a)
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    c=g.add_vertix('C')
    d=g.add_vertix('D')
    
    g.add_edge(a,c)
    # g.add_edge(b,d)
    # g.add_edge(b,e)
    # g.add_edge(e,d)
    # g.add_edge(e,c)

    # print(g.get_all_vertices_with_edges())

    # neighbors=[vertix.value for vertix in g.get_neighbors(a)]
    # print(neighbors)
    # vertices=[vertix.value for vertix in g.get_neighbors()]
    # print(vertices)
    
    print(g.get_all_neighbors())
    