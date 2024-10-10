# min, max 함수 이용
n, m = map(int, input().split())

result = 0

for i in range (0,n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result, min_value)

print(result)

#나는 작은 것들을 다 빼서 비교했지만 여기서는 그때 그때 비교 => 코드가 짧아짐