#1이 될 때까지
#입력 25 5
n, k = map(int, input().split())

count = 0

while True:
    if n%k == 0:
        n= n/k
        count = count + 1
    elif n != 1 and not n%k != 0:
        n = n-1
        count = count + 1
    elif n == 1:
        break

print(count)

#해결방법 : 1이 될 때까지 => while 문 사용 , 1이 된다면 break
#          1을 빼는 것보단 나누는 것이 1에 도달하기 가장 빠름 => K로 나누는 것을 최대한 사용

#문제점: n이 매우 커진다면 시간 복잡도가 커짐  => 1을 한 번 씩 K로 나누어 떨어질 때까지 뺴야하기 때문.... => K로 나누어 떨어질 때까지 한 번에 뺀다면 계산 횟수를 매우 줄일 수 있음 
