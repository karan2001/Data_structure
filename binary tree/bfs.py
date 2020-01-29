graph={
    "A":["B","C"],
    "B":["A","D","E"],
    "C":["A","F"],
    "D":["B"],
    "E":["B","F"],
    "F":["C","E"]
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")

        for neighbours in graph[s]:
            if neighbours not in visited:
                visited.append(neighbours)
                queue.append(neighbours)

bfs(visited,graph,"F")
print(visited)

print(queue)