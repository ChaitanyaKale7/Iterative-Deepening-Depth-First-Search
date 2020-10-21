

def iddfs(visted, graph, current, depth):
    visited[current] = 1
    if current == goal_node:
        global goal_found 
        goal_found = 1
        
    depth = depth - 1
    if depth >= 0:
        for i in range(n): #checks for all the edges of given vertex
            if graph[current][i] == 1 and visited[i] != 1: #if edge exists and vertex is not visited 
                parent[i] = current
                iddfs(visited, graph, i,depth)
    else:
        return True  

# Prints path from start node to goal node
def print_path(vertex):
    path=[]
    while parent[vertex] != -1:
        path.append(vertex)
        vertex = parent[vertex]
    path.append(vertex) 
    path.reverse()
    for i in path:
        print(i,end = '')
        print('-',end = '') 

n=7  #No of nodes present i.e 0-6
graph = [[0,1,1,0,1,0,0], 
         [1,0,0,1,0,1,0], 
         [1,0,0,0,0,0,1], 
         [0,1,0,0,0,0,0],
         [1,0,0,0,0,1,0],
         [0,1,0,0,1,0,0],
         [0,0,1,0,0,0,0]]

visited = [0,0,0,0,0,0,0] #list of visited vertices (1- visited, 0-unvisited)

current = 0     #the current node, initialized with starting node i.e 0

parent = 7*[0]  #list which consists parent of each node
parent[0] = -1  #parent of root is -1

goal_node = 5
global goal_found 
goal_found = 0

for level in range(3):  #iterate over no. of levels present
    if goal_found == 0:
        iddfs(visited, graph, current,level)
        visited = [0,0,0,0,0,0,0] #initialize all vertices as unvisited i.e 0
    elif goal_found == 1:
        break

if goal_found == 0:
    print('Goal Node not found')
else:
    print('Goal node found in level ',level)
    print_path(goal_node)
