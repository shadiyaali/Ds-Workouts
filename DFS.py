from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)  # Do whatever operation you want with the node
            visited.add(node)
            queue.extend(graph[node])

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

bfs(graph, 'B')
 
                 

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
    
#     visited.add(start)
#     print(start)  # Do whatever operation you want with the node

#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)

# # Example usage:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['E'],
#     'D': [],
#     'E': []
# }

# dfs(graph, 'A')
# dfs(graph,"B")
