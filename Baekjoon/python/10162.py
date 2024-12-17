t = int(input())

times = [300, 60, 10]

if not t % 10 == 0:
    print("-1") 
else:
    for time in times:
        q = t // time
        t = t % time
        if time == 10:
            print(q)
        else:
            print(q, end = " ")


