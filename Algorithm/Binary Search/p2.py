n = int(input())
have = list(map(int, input().split()))

m = int(input())
want = list(map(int, input().split()))

for i in want:
    if i in have:
        print("yes", end=' ')
    else:
        print("no", end=' ')
