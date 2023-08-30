def add_node(v):
    if v in graph:
        print("already present")
    else:
        graph[v] = []    

graph = {}        
add_node("A")
add_node("B")

print(graph)