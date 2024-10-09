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

#해결방법: K가 1이 아닌 이상 숫자 배열을 내림차순으로 나열했을 때 인텍스 0, 1 애들만 사용함
#         따라서 연속으로 더한 횟수만 고려해서 그 횟수가 K보다 작을 떄는 인덱스 0인 애를 
#         연속으로 더한 횟수가 K일 때만 인덱스가 1인 애를 더하면 됨

#Big-O 시간 복잡도는 더하는 횟수 M에 영향을 받을 것이기에 O(M)이다.

#그리디의 정당성


