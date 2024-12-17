n = int(input())
store = list(map(int, input().split()))

count = 0
start = 0
for i in store:
    if i == start:
        count = count + 1
        start = start + 1
        if start == 3:
            start = 0

print(count)
