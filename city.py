from collections import defaultdict

def prepare_data(filename):
    graph = defaultdict(list)
    file = open(filename,"r")
    dataset = [x.split(",") for x in file.read().splitlines()]
    for line in dataset:
        graph[line[0]].append([line[1],int(line[2]),int(line[3])])
        graph[line[1]].append([line[0],int(line[2]),int(line[3])])
    return graph

def give_neighbors(graph,state):
    return graph[state]

def choose_leaf(frontier,type):
    if type == "BFS":
        leaf = frontier.pop(0)
        return leaf
def goaltest(leaf,goal):
    if leaf[0]==goal:
        return True

def expand(graph,leaf,explored,frontier):
    neighbors = give_neighbors(graph,leaf[0])
    for neighbor in neighbors:
        if (neighbor[0] not in [x[0] for x in explored]) and (neighbor[0] not in [x[0] for x in frontier]):
            frontier.append(neighbor)

def search(graph,start,goal,type):
    frontier = [[start,0,0]]
    explored = []
    action=[]
    while(1):
        if len(frontier)==0:
            return "Failure"
        leaf = choose_leaf(frontier,type)
        action.append(leaf)
        if goaltest(leaf,goal):
            return action
        explored.append(leaf)
        expand(graph,leaf,explored,frontier)


graph = prepare_data("NS_Dataset_1.csv")
for item in graph:
    print(item)
start = input("Choose Start state EXACTLY as in the list: ")
goal = input("Choose goal state EXACTLY as in the list: ")
type = input("Choose search type: 'BFS' 'DFS' 'GBFS' 'A*' :")
print(search(graph,start,goal,type))
