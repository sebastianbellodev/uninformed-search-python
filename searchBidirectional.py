import queue

map = {
    'Oradea' : {'Zerind': 71, 'Sibiu': 151},
    'Zerind' : {'Oradea': 71, 'Arad': 75},
    'Arad' : {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara' : {'Arad': 118, 'Lugoj': 111},
    'Lugoj' : {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia' : {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta' : {'Mehadia': 75, 'Craiova': 120},
    'Craiova' : {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea' : {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Sibiu' : {'Oradea': 151, 'Arad': 140, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Fagaras' : {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti' : {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest' : {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu' : {'Bucharest': 90},
    'Urziceni' : {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova' : {'Urziceni': 98, 'Eforie': 86},
    'Eforie' : {'Hirsova': 86},
    'Vaslui' : {'Urziceni': 142, 'Iasi': 92},
    'Iasi' : {'Vaslui': 92, 'Neamt': 87},
    'Neamt' : {'Iasi': 87}
}
def searchBidirectional(cityStart, cityObjective):
    visited_top = []
    visited_top.append(cityStart)
    visited_bottom = []
    visited_bottom.append(cityObjective)
    queueAux_top = queue.Queue()
    queueAux_bottom = queue.Queue()
    
    pathAux_top = {cityStart:None}
    pathAux_bottom = {cityObjective:None}
    path = recursiveBidirectional(map, cityStart, cityObjective, visited_top, visited_bottom, queueAux_top, queueAux_bottom, pathAux_top, pathAux_bottom)
    print(path)
    
def recursiveBidirectional(
    graph, cityCurrent_top, cityCurrent_bottom, visited_top, visited_bottom, 
    queueAux_top, queueAux_bottom, pathAux_top, pathAux_bottom):
    ##Caso base
    ## Si coinciden en el moemnto exacto unen sus caminos de otra forma ya sabemos ciertos caminos de ciudades visitadas
    ##Tanto la parte de arriba como la parte de abajo por lo que si es que alguno de los dos recorridos coincide
    ##Con alguna ciudad ya visitada entonces ya se encontro el camino
    if (cityCurrent_top == cityCurrent_bottom or cityCurrent_top in visited_bottom or cityCurrent_bottom in visited_top): 
        ##Se requiere conocer desde que punto se encontro el camino y definir una ciudad auxiliar
        ##Esto se debe a que no sabemos porque condición se encontro el camino
        ##Esta nos permite recorrer el camino en ambas direcciones para ir construyendolo
        ##Desde la posición que se encontró hacia la posición inicial
        if(cityCurrent_top == cityCurrent_bottom):
            cityAux_top = cityCurrent_top
        elif(cityCurrent_top in visited_bottom):
            cityAux_top = cityCurrent_top
        elif(cityCurrent_bottom in visited_top):
            cityAux_top = cityCurrent_bottom
        cityAux_bottom = cityAux_top
        ##Variables para construir los caminos de las dos direcciones
        path_top = {}
        path_bottom = {}  
        ##Ciclos que permiten ir reconstruyento el camino                    
        while(cityAux_top != None):                     
            path_top[cityAux_top] = pathAux_top[cityAux_top]
            cityAux_top = pathAux_top[cityAux_top]
        while(cityAux_bottom != None):    
            path_bottom[cityAux_bottom] = pathAux_bottom[cityAux_bottom]
            cityAux_bottom = pathAux_bottom[cityAux_bottom]
        ##Se unen los caminos de las dos direcciones
        finalPath = []                             
        for city in path_top.keys():                   
            finalPath.append(city)
        finalPath.reverse()                     ##Al ser un camino inverso para obtener el camino correcto se invierte             
        for city in path_bottom.keys():        
            finalPath.append(city)
        return finalPath
    else:                      
        ##Caso recursivo
        leafs_top = graph[cityCurrent_top]                 
        for leaf in leafs_top:                          
            if leaf not in visited_top:                
                visited_top.append(leaf)                
                queueAux_top.put(leaf)
                pathAux_top[leaf] = cityCurrent_top
        leafs_bottom = graph[cityCurrent_bottom]                 
        for leaf in leafs_bottom:                          
            if leaf not in visited_bottom:                
                visited_bottom.append(leaf)                
                queueAux_bottom.put(leaf)
                pathAux_bottom[leaf] = cityCurrent_bottom 
        nextCity_top = queueAux_top.get()
        nextCity_bottom = queueAux_bottom.get()
        return recursiveBidirectional(graph, nextCity_top, nextCity_bottom, visited_top, visited_bottom, queueAux_top, queueAux_bottom, pathAux_top, pathAux_bottom)  ##Recursión


searchBidirectional('Neamt', 'Eforie')
