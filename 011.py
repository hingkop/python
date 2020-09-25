#소수 구하기
#생리 미친놈
def calc_prime(n):
    cnt = 0
    i = 2
    k = 1
    while i < n:
        if check[i] == True:
            print(i)
            j = 1 
            while j < n :
                check[j] = False
                k = k+1
                j = i* k



if __name__=="__main__":
    n = 20 
    calc_prime(n)