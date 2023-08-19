import pytest
from graph.graph import Graph

# 1. Vertex can be successfully added to the graph
def test_add_vertex():
    g=Graph()
    a=g.add_vertix('A')
    actual = g.breadth_first(a)
    expected = ['A']
    assert actual == expected

# 2. An edge can be successfully added to the graph
def test_add_edge():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    g.add_edge(a,b)
    actual = g.get_neighbors(a)[0].__str__()
    expected = "Edge to: B, Weight: 0"
    assert actual == expected

# 3. A collection of all vertices can be properly retrieved from the graph
def test_collection_of_vertices():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    vertices=[vertix.value for vertix in g.get_vertices()]
    actual = vertices
    expected = ['A', 'B', 'E']
    assert actual == expected

# 4. All appropriate neighbors can be retrieved from the graph
def test_get_all_neighbors():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    c=g.add_vertix('C')
    d=g.add_vertix('D')
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
   
    actual = g.get_all_neighbors().__str__()
    expected = """Edge to: C, Weight: 0,Edge to: D, Weight: 0,Edge to: E, Weight: 0,Edge to: B, Weight: 0,Edge to: D, Weight: 0,Edge to: C, Weight: 0,Edge to: A, Weight: 0,Edge to: E, Weight: 0,Edge to: B, Weight: 0,Edge to: E, Weight: 0,"""
    assert actual == expected

def test_get_neighbors():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    c=g.add_vertix('C')
    d=g.add_vertix('D')
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
   
    actual = g.get_neighbors(a)[0].__str__()
    expected = "Edge to: C, Weight: 0"
    assert actual == expected

# 5. Neighbors are returned with the weight between vertices included
def test_get_all_vertices_with_neighbors():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    c=g.add_vertix('C')
    d=g.add_vertix('D')
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
   
    actual = g.get_all_vertices_with_edges().__str__()
    expected = "{|A,Edge to: C, Weight: 0,|B,Edge to: D, Weight: 0,Edge to: E, Weight: 0,|E,Edge to: B, Weight: 0,Edge to: D, Weight: 0,Edge to: C, Weight: 0,|C,Edge to: A, Weight: 0,Edge to: E, Weight: 0,|D,Edge to: B, Weight: 0,Edge to: E, Weight: 0,}"
    assert actual == expected

# 6. The proper size is returned, representing the number of vertices in the graph
def test_get_size():
    g=Graph()
    a=g.add_vertix('A')
    b=g.add_vertix('B')
    e=g.add_vertix('E')
    c=g.add_vertix('C')
    d=g.add_vertix('D')
    g.add_edge(a,c)
    g.add_edge(b,d)
    g.add_edge(b,e)
    g.add_edge(e,d)
    g.add_edge(e,c)
   
    actual = g.size()
    expected = 5
    assert actual == expected

# 7. A graph with only one vertex and edge can be properly returned
def test_one_vertix_one_edge():
    g=Graph()
    a=g.add_vertix('A')
    g.add_edge(a,a)
     
    actual = g.breadth_first(a)
    expected = ['A']
    assert actual == expected