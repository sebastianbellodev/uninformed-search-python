import queue
import time
import psutil
import romania

graph = romania.map
time = time.process_time()

def getBFS(root, goal):
    explored = []
    path = {root:None}
    explored.append(root)
    auxQueue = queue.Queue()
    auxPath = {root:None}
    path = setBFS(graph, root, goal, explored, auxQueue, auxPath)
    print(path)
    
def setBFS(graph, state, goal, explored, auxQueue, auxPath):
    ## Base case
    if state == goal:
        ## Build final path when the goal is reached
        path = {}
        ## Changeable variable to go through the path 
        auxState = goal
        ## Loop to search the path that was followed                      
        while(auxState != None):
            path[auxState] = auxPath[auxState]
            auxState = auxPath[auxState]
        ## Create the final path
        finalPath = []
        ## Extract the key values from the path and add them to the list
        for city in path.keys():
            finalPath.append(city)
        ## Reverse the list to get the correct path
        finalPath.reverse()
        return finalPath
    ## Recursive case
    else:
        ## Extract the leaf nodes from the graph
        leafs = graph[state]
        ## Push the leaf nodes into the queue
        for leaf in leafs:
            ## Expand the leaf nodes
            if leaf not in explored: 
                ## If a leaf node has already been explored, it is not explored again               
                explored.append(leaf)
                auxQueue.put(leaf)
                ## Save the path between two cities for later rebuilding
                auxPath[leaf] = state
        ## Establish the next city to visit
        nextState = auxQueue.get()
        ## Recursive call
        return setBFS(graph, nextState, goal, explored, auxQueue,auxPath)

def getPerformance(): 
    cpu = psutil.cpu_percent(interval=1)
    print("CPU: " + str(cpu) + "%")
    print("Time: " + str(time) + "s")

getBFS('Arad', 'Neamt')  
getPerformance()
