t = int(input())
remains = []

for i in range(t):
    remains.append(int(input()))

coins = [25, 10, 5 ,1]

for remain in remains:
    for coin in coins:
        count = remain // coin
        remain = remain % coin
        if coin == 1:
            print(count)
        else:
            print(count, end= ' ')
