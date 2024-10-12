#변수가 정수형 같은 숫자로 이루어져있을 때 그때 변수에 특정 숫자가 있는 것을 찾기는 어렵다. 하지만 그 숫자를 string으로 바꿀 수 있다면 문자열로 쉽게 찾을 수 있다.
n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str (j) + str (k):
                count = count + 1

print(count)

#for문을 이렇게.... + str...
#완전 탐색(Brute Forcing)

