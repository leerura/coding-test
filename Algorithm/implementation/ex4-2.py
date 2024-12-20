#시각 문제
#입력 5
#경우의 수 문제 같아서 여집합을 생각했음
n = int(input())

all = 1 * (n+1) * 6 * 10 * 6 * 10
not_three = 0

if n == 3:
    not_three = 1*n*5*9*5*9
elif n > 3:
    not_three = 1*n*5*9*5*9
elif n < 3:
    not_three = 1*(n+1)*5*9*5*9

print (all - not_three)



#1쨰 자리 0
#2째 자리 0 1 2 3 4 5
#3째 자리 0 1 2 3 4 5
#4째 자리 0 1 2 3 4 5 6 7 8 9
#5째 자리 0 1 2 3 4 5
#6째 자리 0 1 2 3 4 5 6 7 8 9

#해결방법: 경우의수 = 전체 - 3이 없는 경우의 수
#문제점:1. n이 두 자리 수면 해결하지 못함(알고리즘은 떠오르나 구현이 복잡함)
#       2. 여집합은 사람이 풀기 좋은 방법임 => 여기서 계산은 어쩌파 컴퓨터가 함 => 굳이 여집합 x

#시간 복잡도: 여기선 계산을 3번 하기에 O(3)이라고 볼 수 있다.