#소수 구하기
#아니 모르겠어서 시키는 대로 했잖아 왜 안되는건데 나 화나.
True = 1
False = 0
def calc_prime(n):
    check = [True] * 1000
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

            k = 1
        i = i+1

if __name__=="__main__":
    n = 20 
    calc_prime(n)