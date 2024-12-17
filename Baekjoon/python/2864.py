a, b = map(str, input().split())

first = list(map(int, a))
second = list(map(int, b))

for i in range(len(first)):
    if first[i] == 6:
        first[i] = 5

for i in range(len(second)):
    if second[i] == 6:
        second[i] = 5
    
f = ''.join(map(str, first))
s = ''.join(map(str, second))

print(int(f)+int(s), end = ' ')

for i in range(len(first)):
    if first[i] == 5:
        first[i] = 6

for i in range(len(second)):
    if second[i] == 5:
        second[i] = 6

f = ''.join(map(str, first))
s = ''.join(map(str, second))

print(int(f)+int(s))




    
    
    

    