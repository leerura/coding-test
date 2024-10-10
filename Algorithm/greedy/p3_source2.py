n, m = map(int, input().split())

result = 0

for i in range(0,n):
    data = list(map(int,input().split()))
    min_value = 10001
    for i in data:
        min_value = min(i, min_value)
    result = max(result, min_value)

#min 함수가 있는데 굳이 2중 for문을 써야할까??