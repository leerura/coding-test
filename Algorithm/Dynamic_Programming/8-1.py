#재귀적 방법을 이용한 피보나치 수열
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(99))

#숫자가 커지면 너무 오래 걸림