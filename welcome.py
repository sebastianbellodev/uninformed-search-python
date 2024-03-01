ORADEA = "Oradea"
SIBIU = "Sibiu"
ZERIND = "Zerind"
ARAD = "Arad"
TIMISOARA = "Timisoara"
FAGARAS = "Fagaras"
RIMNICU = "Rimnicu"
LUGOJ = "Lugoj"
MECHADIA = "Mechadia"
DOBRETA = "Dobreta"
CRAIOVA = "Craiova"
PITESTI = "Pitesti"
BUCHAREST = "Bucharest"
GIURGIU = "Giurgiu"
URZICENI = "Urziceni"
HIRSOVA = "Hirsova"
VASLUI = "Vaslui"
EFORIE = "Eforie"
IAISI = "Iasi"
NEAMT = "Neamt"

ROUTES = [(ORADEA, SIBIU, 151)]

def welcome():
    print("Welcome to % s!" % ROUTES[0][1])
    print("Have a safe trip!")
welcome()