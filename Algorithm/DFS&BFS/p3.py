n,m = map(int,input().split())

graph = []
for i in range(n):
     graph.append(list(map(int,input().split())))

def dfs(x,y):
     if x <= -1 or x >=n or y <= -1 or y >=n:
          return False
     if graph[x][y] == 0:
          dfs(x-1,y)
          dfs(x+1,y)
          dfs(x, y+1)
          dfs(x,y-1)
          return True
     return False

result = 0

for i in range (n):
     for j in range(m):
          if dfs(i,j) == True:
               result = result + 1

print(result)

#최대한 간단히 생각할 수 있어야함...

 
