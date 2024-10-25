#순차 탐색(Sequential_Search)
n = int(input())
name = input()
array = input().split()

def sequential_search(n,name,array):
    for i in range(n):
        if name == array[i]:
            return i
    
print("인덱스: ", sequential_search(n, name, array))