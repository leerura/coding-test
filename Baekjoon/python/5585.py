n = int(input())

remain = 1000 - n

coins = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coins:
    q = remain // coin
    remain = remain % coin
    
    count = count + q
    if remain == 0:
        break

print(count)
