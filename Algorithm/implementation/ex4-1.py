#상하좌우 문제
#입력 5
#     R R R U D D
#평소에 사용하는 좌표계가 아니여서 헷갈렸음

n = int(input())
data = list(map(str,input().split())) #어짜피 split이 str 객체의 list를 반환하기에 map함수 쓸 필요가 없음

x,y = 1,1

for i in data:
    if (x==1 and i == 'U') or (x==n and i == 'D') or (y==1 and i == 'L') or (y==n and i == 'R'):
        print("did not move") #continue로 대체 가능
    elif i == 'U':
        x = x-1
    elif i == 'D':
        x = x+1
    elif i == 'L':
        y = y-1
    elif i == 'R':
        y = y + 1

print(x, y)

#해결 방법: 움직이지 못하는 상황을 먼저 확인
#빅오 시간복잡도 => 최대 움직이는 횟수가 연산 수 => O(이동횟수) 