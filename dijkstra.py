def minDistance(V, dist, visited):
    min_value = float('inf')
    min_index = -1
    for v in range(V):
        if(dist[v] < min_value and not visited[v]):
            min_value = dist[v]
            min_index = v
    return min_index

def dijkstra(Graph, Src, V):
    dist = [float('inf')] * V
    dist[Src] = 0
    visited = [False] * V
    
    for route in range(V):
        u = minDistance(V, dist, visited)
        if u == -1:
            break
        visited[u] = True
        for v in range(V):
            if (Graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + Graph[u][v]):
                dist[v] = dist[u] + Graph[u][v]
                
    print("Vertex \t Distance")
    for node in range(V):
        print(node, '\t\t', dist[node])

# Example usage
n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (one row at a time):")
Graph = []
for i in range(n):
    values = list(map(int, input().split()))
    Graph.append(values)
Src = int(input("Enter the source vertex: "))
dijkstra(Graph, Src, n)
