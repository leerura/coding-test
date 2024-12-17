n = int(input())
height = list(map(int,input().split()))

result = 0
count = 0
for i in range(len(height)):
    if result < count:
        result = count
    bow = height[i]
    count = 0
    for j in range(i + 1, len(height)):
        if bow > height[j]:
            count = count + 1
        
print(result)