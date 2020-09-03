#3과 5의 배수 계산하기
def f(n):
    i = 1
    while i <= n:
        if(i % 3==0) and (i % 5==0):
            print("%d"%(i))
        i = i+1
if __name__ == '__main__':
    f(100)