#bisect
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_right(a,x))
print(bisect_left(a,x))

#bisect_right: 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
#bisect_right: 정렬된 순서를 유지하면서 배열 a에 x를 삽일할 가장 오른쪽 인덱스를 반한