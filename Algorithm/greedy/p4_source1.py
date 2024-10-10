#입력 25 5
n, k = map(int, input().split())

count = 0

while n >= k :
    while n % k != 0:
        n = n-1
        count = count +1
    n = n //k
    count = count + 1

while n < 1 :
    n = n -1
    count = count + 1

print(count)


