#왕실의 나이트 문제
#입력: a1
position = list(map(str,input()))

x_position = position[0]
y_position = int(position[1])

x = ['a', 'b', 'c', 'd,', 'e', 'f', 'g', 'h']
#x좌표도 숫자로 바꾸고 싶음
for i in range (8):
    if x_position == x[i]:
        x_position = i+1
#인덱스에 맞춰 L 움직임을 표현
movex = [ 2 , 2 , -2, -2, 1, -1 , 1, -1]
movey = [1, -1 , 1, -1, 2 , 2 , -2, -2]
count = 0


for i in range(8):
    nx = x_position + movex[i]
    ny = y_position + movey[i]
    if nx < 1 or nx > 8 or ny <1 or ny >8:
        continue
    count = count + 1


print(count)

#해결방법: 앞서 푼 경로 문제로 만들 수 있다고 생각함 => 1. 위치가 알파벳으로 주어졌는데 숫자로 바꿈
#                                                   2. 움직임을 표현


