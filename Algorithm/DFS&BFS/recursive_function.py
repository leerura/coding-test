def recursive_function(i):
    if i == 100:
        return
    print(i,'번째 함수에서', i+1, '반째를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 종료')

recursive_function(1)