#큰 수의 법칙
#입력 5 8 3
#     2 4 5 4 6
import time

N, M, K = map(int, input().split()) #N = 배열 크기, M = 더하기 시행 횟수 , K = 같은 수를 최대한 더할 수 있는 횟수
numbers = list(map(int, input().split())) # 리스트로 만들기

start_time = time.time()

count = 0 # 결과
count_K = 0 # 연속으로 더한 횟수 카운트

#내림차순 정리
sorted_numbers = sorted(numbers, reverse=True)


for i in range (0,M): #더하는 횟수 만큼 실행
    if count_K < K+1 and not count_K == 3: #연속으로 더한 횟수가 3이 되기 전까진 가장 큰수를 더함
        count = count + sorted_numbers[0]
        count_K = count_K + 1
    elif count_K == K: # 연속으로 더한 횟수가 3이면 가장 큰 수 다음으로 큰 수를 더함
        count = count + sorted_numbers[1]
        count_K = 0

print(count)

end_time = time.time()

print("소요 시간: " , end_time - start_time)



