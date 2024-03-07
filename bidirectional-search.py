import queue
import time
import psutil
import romania

graph = romania.map
time = time.process_time()

def getBS(root, goal):
    exploredTop = []
    exploredTop.append(root)
    exploredBottom = []
    exploredBottom.append(goal)
    auxTopQueue = queue.Queue()
    auxBottomQueue = queue.Queue()
    auxTopPath = {root:None}
    auxBottomPath = {goal:None}
    path = setBS(graph, root, goal, exploredTop, exploredBottom, auxTopQueue, auxBottomQueue, auxTopPath, auxBottomPath)
    print(path)
    
def setBS(graph, topState, bottomState, exploredTop, exploredBottom, auxTopQueue, auxBottomQueue, auxTopPath, auxBottomPath):
    ## Base case
    ## If the two paths meet at the same time, they join their paths. Otherwise, we know certain paths of visited cities both the top and bottom parts
    ## So if one of the two paths coincides with a visited state, then the path is already found
    if (topState == bottomState or topState in exploredBottom or bottomState in exploredTop):
        ## We need to know from which point the path was found and define an auxiliary state, because we do not know why the path was found 
        ## This line help us to know from which point the path was found, from the current state to the initial state
        if(topState == bottomState):
            auxTopState = topState
        elif(topState in exploredBottom):
            auxTopState = topState
        elif(bottomState in exploredTop):
            auxTopState = bottomState
        auxBottomState = auxTopState
        ## Variables to build the paths for both directions
        topPath = {}
        bottomPath = {}
        ## Loop that allows to rebuild the path  
        while(auxTopState != None):                     
            topPath[auxTopState] = auxTopPath[auxTopState]
            auxTopState = auxTopPath[auxTopState]
        while(auxBottomState != None):    
            bottomPath[auxBottomState] = auxBottomPath[auxBottomState]
            auxBottomState = auxBottomPath[auxBottomState]
        ## Merge the paths of the two directions
        finalPath = []                             
        for state in topPath.keys():                   
            finalPath.append(state)
        ## Reverse the list to get the correct path
        finalPath.reverse()
        finalPath.pop()       
        for state in bottomPath.keys():        
            finalPath.append(state)
        return finalPath
    ## Recursive case
    else:                      
        ## Extract the leaf nodes from the graph
        topLeafs = graph[topState]  
        ## Push the leaf nodes into the queue               
        for leaf in topLeafs:    
            ## Expand the leaf nodes                        
            if leaf not in exploredTop:
                # If a leaf node has already been explored, it is not explored again                 
                exploredTop.append(leaf)                
                auxTopQueue.put(leaf)
                ## Save the path between two cities for later rebuilding
                auxTopPath[leaf] = topState
        ## Extract the leaf nodes from the graph
        bottomLeafs = graph[bottomState]
        ## Push the leaf nodes into the queue                 
        for leaf in bottomLeafs:                          
            if leaf not in exploredBottom:
                # If a leaf node has already been explored, it is not explored again                  
                exploredBottom.append(leaf)                
                auxBottomQueue.put(leaf)
                ## Save the path between two cities for later rebuilding
                auxBottomPath[leaf] = bottomState 
        ## Establish the next city to visit        
        nextTopState = auxTopQueue.get()
        nextBottomState = auxBottomQueue.get()
        ## Recursive call
        return setBS(graph, nextTopState, nextBottomState, exploredTop, exploredBottom, auxTopQueue, auxBottomQueue, auxTopPath, auxBottomPath)

def getPerformance(): 
    cpu = psutil.cpu_percent(interval=1)
    print("CPU: " + str(cpu) + "%")
    print("Time: " + str(time) + "s")

getBS('Arad', 'Neamt') 
getPerformance()
