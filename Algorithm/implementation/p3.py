n, m = map(int,input().split())
#현위치, 방향
row,column,direction = map(int,input().split())
#방문 정보
d = [[0]*m for _ in range(n)]

#전체 맵 정보
#위치와 육지 바다 여부를 따로 저장할 필요가 없음 => 리스트의 인덱스가 위치와 관련
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#북동남서 방향 인덱스에 맞춰서 이동 설정
drow = [-1 , 0 , 1 ,0]
dcolumn = [0, 1 , 0, -1]

def turn_left():
    global direction
    direction= direction-1
    if direction == -1:
        direction = 3

count = 1 
turn_time = 0

while True:
    turn_left()
    nrow = row + drow[direction]
    ncolumn = column + dcolumn[direction]
    if d[nrow][ncolumn] == 0 and array[nrow][ncolumn] == 0:
        d[nrow][ncolumn] = 1
        row = nrow
        column = ncolumn
        count = count + 1
        turn_time = 0
        continue
    else:
        turn_time = turn_time + 1
    if turn_time == 4:
        nrow = row - drow[direction]
        ncolumn = column - dcolumn[direction]
        if array[nrow][ncolumn] == 0:
            row = nrow
            column = ncolumn
        else:
            break
        turn_time = 0

print(count)
        

#재귀적 방법으로도 할 수 있지 않을까??









        

        


#tuple(map(int,input().split()))

