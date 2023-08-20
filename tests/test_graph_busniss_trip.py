import pytest
from graph_busniss_trip.graph import Graph
from graph_busniss_trip.graph_business_trip import business_trip

g=Graph()
Pandora=g.add_vertix('Pandora')
Arendelle=g.add_vertix('Arendelle')
Metroville=g.add_vertix('Metroville')
New_Monstropolis=g.add_vertix('New_Monstropolis')
Narnia=g.add_vertix('Narnia')
Naboo=g.add_vertix('Naboo')
    
g.add_edge(Pandora,Arendelle,150)
g.add_edge(Pandora,Metroville,82)
g.add_edge(Narnia,Metroville,37)
g.add_edge(Narnia,Naboo,250)
g.add_edge(Metroville,Arendelle,99)
g.add_edge(Metroville,New_Monstropolis,105)
g.add_edge(Metroville,Naboo,26)
g.add_edge(Arendelle,New_Monstropolis,42)
g.add_edge(Naboo,New_Monstropolis,73)





    
def test_case_1():
    case_1=[Metroville, Pandora]
    actual = business_trip(g,case_1)
    expected = "$82"
    assert actual == expected

def test_case_2():
    case_2=[Arendelle, New_Monstropolis,Naboo]
    actual = business_trip(g,case_2)
    expected = "$115"
    assert actual == expected

def test_case_3():
    arr3=[Naboo, Pandora]
    actual = business_trip(g,arr3)
    expected = None
    assert actual == expected

def test_case_4():
    case_4=[Narnia, Arendelle, Naboo]
    actual = business_trip(g,case_4)
    expected = None
    assert actual == expected

