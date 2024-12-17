n = 3

for i in range(1,n+1):
    l,p,v = map(int, input().split())
    if l == 0:
        break
    q = v//p
    r = v%p
    if l < r:
        result = q*l + l
    else:
        result = q*l + r
    print(f"Case {i}: {result}")

