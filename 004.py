#재귀로 n~1 출력
def f(n):
    print (n)
    if n > 1:
        f(n-1)
 
if __name__ == '__main__':
    f(10)