graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

visited = []

def dfs(visited,graph,node):
    
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(visited,graph,n)


dfs(visited,graph1,'S')

print(visited)
