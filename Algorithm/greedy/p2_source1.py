import time

N, M, K = map(int, input().split()) #N = 배열 크기, M = 더하기 시행 횟수 , K = 같은 수를 최대한 더할 수 있는 횟수
data = list(map(int, input().split())) # 리스트로 만들기

start_time = time.time()

data.sort() #data.sort()는 none을 반환함으로 data = data.sort()하면 안됨
#어짜피 가장 큰 수 2개만 쓸 것임
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result = result + first
        M = M-1
    if M == 0:
        break
    result = result + second
    M = M-1

print(result)

end_time = time.time()

print("소요시간: ", end_time-start_time)

#반복할 때 for문 말고 while을 쓰는 것도!!