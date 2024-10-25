n = int(input())

array = []
for i in range(n):
    name,score = map(str, input().split())
    array.append((name,score))

array = sorted(array, key=lambda data : int(data[1]))

for student in array:
    print(student[0], end=' ')