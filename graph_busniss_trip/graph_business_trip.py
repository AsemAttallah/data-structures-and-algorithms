def business_trip(graph,city_list):
    '''
    Arguments: graph, array of city names
    Return: the cost of the trip (if it's possible) or None (if not)
    This function for calculation the cost of the trip if it is possible
    '''
    total=0
    counter=1
    for i in range(len(city_list)):
        if i+1 < len(city_list):
            second=graph.get_neighbors(city_list[i])
            for j in range(len(second)):
                if str(city_list[i+1].value)==str(second[j]):
                    counter+=1
                    total=total+second[j].edge_weight()
            if counter==len(city_list):
                return "$"+str(total)
    return None

                




if __name__=="__main__":
    from graph import Graph 
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

    arr=[Metroville, Pandora]
    arr2=[Arendelle, New_Monstropolis,Naboo]
    arr3=[Naboo, Pandora]
    arr4=[Narnia, Arendelle, Naboo]
    arr5=[Arendelle, New_Monstropolis, Pandora]
    arr6=[Pandora,Naboo]
    print(business_trip(g,arr3))

