#숫자 카드 게임
#문제 이해가 힘들었음
#입력 3 3
#     3 1 2 
#     4 1 4 
#     2 2 2

n, m = map(int, input().split())

array = [] #행과 열 데이터 담을 array
for i in range (0,n):
    array.append(list(map(int, input().split())))

print(array)

array2 = [] #각 행 중 가장 작은 데이터 담을 array

for i in array:
    i.sort()
    a = i[0]
    array2.append(a)

array2.sort(reverse=True) #오름차순으로 정리
print(array2[0])

#해결방법: 각각의 행을 리스트로 만들고 그 각각의 행들의 가장 작은 요소들을 비교...

