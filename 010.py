#약수 구하기
def solve (n):
    ans = 0
    i=1 
    while i <=n:
        if n % i ==0:
            print(i)
        i = i+1

if __name__=="__main__":
<<<<<<< HEAD
    n = int(input("입력:"))
    solve(n)
=======
    n = int(input("입력"))
    solve(n)
>>>>>>> 979a6d37a71a0c95f8d37b8f54bc55373686d278
