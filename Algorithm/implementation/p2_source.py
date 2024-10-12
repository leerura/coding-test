#나와 다른 점: 1. 알파벳으로 표현된 x좌표를 숫자로 바꿀 때 ord를 사용함
#             2. 움직임을 표현할 때 리스트 안의 튜플을 넣어서 표현함
#             3. continue를 안 씀 => if문에서 조건에 맞으면 count +1
position = input()
x = int(ord(position[0])) - int(ord('a')) + 1
y = int(position[1])

steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

count = 0

for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count = count + 1

print(count)