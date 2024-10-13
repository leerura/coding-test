#팩토리얼을 반복적 방식과 재귀적 방식으로 구현해보겠다.

#반복적 방법
def iterative(n):
    result_iterative = 1

    for i in range (1,n+1):
        result_iterative = result_iterative * i
    print(result_iterative)

iterative(5)

#재귀적 방법

def recursive(n):
    if n == 1:
        return n
    result = n * recursive(n-1)
    return result


print(recursive(5))
    