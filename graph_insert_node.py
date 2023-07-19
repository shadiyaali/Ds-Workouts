def add_node(v):
    global  node_count
    if v in nodes:
        print("already presnt")
    else:
        node_count = node_count+1 
        nodes.append(v)
        for n in graph:
            n.append(0) 
        temp = []
        for i in range(node_count):
            temp.append(0)   
        graph.append(temp)   
def add_edge(v1,v2):
    if v1 not in nodes:
        print("v1 not present")  
    elif v2 not in nodes:
        print("v2 not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] =1    
def delete_node(v):
    global node_count
    if v not in nodes:
        print("not empty")
    else:
        index1 = nodes.index(v)
        node_count = node_count-1 
        nodes.remove(v) 
        graph.pop(index1)  
        for i in graph:
            i.pop(index1)  

def delete_edge(v1,v2):
    if v1 not in nodes:
        print("not empty") 
    elif v2 not in nodes:
        print("not present")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0
        graph[index2][index1] = 0                   

def DFS(node,visited,graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print("node")
        visited.append(node)
        for i in graph[node]:
            DFS(i,visited,graph)
 


     
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print() 


def print_DFS(start_node):
    visited = []
    DFS(start_node, visited, graph)
 
# visited = set()
# # graph= {}        
nodes = []
graph = []
node_count =0
# print("before adding nodes")
# print(nodes)
# print(graph)
# add_node("A")
# add_node("B")
# print("after adding")
# print(nodes)
# print(graph)
# print_graph()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B")
add_edge("C","D")
add_edge("A","D")
# delete_node("C")
# delete_node("D")
# delete_edge("C","D")

# print_graph()
print_DFS("A")
 