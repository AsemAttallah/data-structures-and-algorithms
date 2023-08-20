# Code challenge 35 : graph
## Approach & Efficiency
* In this challenge I use Adjacency List to represent graph 
* Big O: time complexity = O(n) when n number of vertices and egdes
* Big O: space complexity = O(n) when n number of vertices and egdes
## Solution
* Graph
    * add method : Argument:value, Return: The added vertix, Add a vertix to the graph

            g=Graph()
            a=g.add_vertix('A')
            return a

        
    
    * add edge method :Arguments: (2) vertices to be connected by the edge,weight(optional),Return: None, Adds a new edge between two vertices in the graph if specified, assign a weight to the edge Both vertices should already be in the graph 

            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
    
    * get vertices method : Argument: None, Return: all of the vertices in the graph as a collection (set, list, or similar), Empty collection returned if there are no vertices
        
            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.get vertices()
            return ['A','C']
    
    * size method : Argument: None, Return: The total number of vertices in the graph
        
            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.size()
            return 2
    
    * get neighbors method : Argument: vertix, Return a collection of edge connected to the given vertix, Include the weight of the connection in the returned collection, Empty collection returned if there are no vertices

            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.get_neighbors(a)
            return c
    
    * get all neighbors method : Argument: None, Return all collection of edges, Get all neighbors in the graph

            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.get_all_neighbors()
            return c,a
    

            
    * get all vertices with edges method :Argument: None, Return all collection of vertices and edges, Get all vertices and edges  in the graph

            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.get_all_vertices_with_edges()
            return "{|A,Edge to: C, Weight: 0,|C,Edge to: A, Weight: 0,}"

    * breadth first method : making a breadth first travesing

            g=Graph()
            a=g.add_vertix('A')
            c=g.add_vertix('C')
            g.add_edge(a,c)
            g.breadth_first()
            return ['A','C']
