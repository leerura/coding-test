#BFS 예제
from collections import deque

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    print(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)

        

   

graph = [
    [], #0 node
    [2, 3, 8], #1
    [1, 7], #2
    [1, 4, 5], #3
    [3, 5], #4
    [3, 4], #5
    [7], #6
    [2,6,8], #7
    [1, 7] #8
]

visited=[False] * 9

bfs(graph,1, visited)