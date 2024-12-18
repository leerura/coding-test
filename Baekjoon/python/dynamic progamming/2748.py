n = int(input())
data = [0] * (n+1)

data[1] = 1

for i in range(2, n+1):
    data[i] = data[i-1] + data[i-2]

print(data[n])
