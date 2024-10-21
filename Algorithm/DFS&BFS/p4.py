from collections import deque
n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

#현위치 0,0 최종목적지 n-1,m-1
#오른쪽 아니면 밑으로 가야 최단

queue = deque()
count = 0

