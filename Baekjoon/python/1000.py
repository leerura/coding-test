c = input()
c = c.split()

a = int(c[0])
b = int(c[1])

print(a+b)
# split ==> 리스트를 만든다
# map 함수 map(fuction, iterable) 계속 객체 반환

a,b = map(int, input().split)

print(a+b)
