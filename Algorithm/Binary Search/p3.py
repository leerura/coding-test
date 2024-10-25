n, m = map(int,input().split())
heights = list(map(int,input().split()))

max_height = max(heights)

result = []
for i in range(max_height):
    length = 0
    for height in heights:
        cut = height-i
        if cut < 0:
            cut = 0
        length = length + cut
    result.append(length)

#6을 찾자
result.sort()
print(result)

def binary(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if target < array[mid]:
        return binary(array,target,start,mid-1)
    elif target > array[mid]:
        return binary(array,target,mid+1,end)
    else:
        return mid
    
print((max_height-1) - binary(result,m,0,max_height+1))

#높이가 1부터 10억까지의 정수이기에 높이에 따라 시간초과를 받을 수 있음... => for문 쓰지 않고 바로 이진탐색
    


    
