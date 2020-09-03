#숫자 뒤집기
def f(n):
    if n ==0:
        return 0
    print (n%10.end='')
    f(n//10)