n, m = map(int,input().split())
posi_dic = list(map(int,input().split()))
types = []

count = 0
while True:
    for j in range(m):
        types.append(list(map(int,input().split()))[j])
        count = count + 1
    if count == 4:
        break

print(types)



row_column_types = []

for i in range (1,n+1):
    for j in range (1,m+1):
        row_column_types.append([i,j])


        

        


#tuple(map(int,input().split()))

