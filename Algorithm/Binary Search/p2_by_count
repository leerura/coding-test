#p2 계수정렬

n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

count = [0] * 1000000

for i in have:
    count[i+1] = count[i+1] + 1

for j in want:
    if count[j+1] >= 1:
        print('yes', end=" ")
    else:
        print('no', end=" ")

