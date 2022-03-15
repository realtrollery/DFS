def DFSUtil(v, visited):
    visited.add(v)
    print(v, end=" ")
    for neighbour in graph[v]:
        if neighbour not in visited:
            DFSUtil(neighbour, visited)


def DFS():
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            DFSUtil(vertex, visited)