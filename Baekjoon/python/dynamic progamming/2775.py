t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    data = [[0] * (n+1) for i in range(k+1)]

    for i in range(n+1):
        data[0][i] = i
    
    for k in range(1, k+1):
        for n in range(n+1):
            data[k][n] = sum(data[k-1][0:n+1])
    print(data[k][n])