
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

import queue

def searchRecursiveBFS(cityStart, cityObjective):
    visited = []
    path = {cityStart:None}
    visited.append(cityStart)
    queueAux = queue.Queue()
    pathAux = {cityStart:None}
    path = recursiveBFS(map, cityStart, cityObjective,visited, queueAux, pathAux)
    print(path)
    
def recursiveBFS(graph, cityCurrent, cityObjective, visited, queueAux, pathAux):
    if cityCurrent == cityObjective:                ##Caso base
        path = {}                                   ##Camino Final
        cityAux = cityObjective                     ##Variable que se cambiara para ir recorriendo el camino    
        while(cityAux != None):                     ##Ciclo para buscar el camino que se siguió
            path[cityAux] = pathAux[cityAux]
            cityAux = pathAux[cityAux]
        finalPath = []                              ##Camino que será el resutlado
        for city in path.keys():                    ##Extrae los valores clave del path y los añade a la lista finalPath
            finalPath.append(city)
        finalPath.reverse()                         ##Invierte el orden de la lista
        return finalPath
    else:                                           ##Caso recursivo
        leafs = graph[cityCurrent]                  ##Extraemos los nodos hijos del grafo para ir construyendo el camino a seguir
        for leaf in leafs:                          ##Asignamos los nodos a una cola
            if leaf not in visited:                 ##Se realiza esto para seguir un recorrido en orden de amplitud
                visited.append(leaf)                ##Si ya se recorrio un nodo no se vuleve a visitar
                queueAux.put(leaf)
                pathAux[leaf] = cityCurrent         ##Se crea un diccionario con el camino entre dos ciudades, posteiormente se reconstruirá este camino
        nextCity = queueAux.get()                   ##Se obtiene la siguiente ciudad a visitar
        return recursiveBFS(graph, nextCity, cityObjective, visited, queueAux,pathAux)  ##Recursión
    
    
