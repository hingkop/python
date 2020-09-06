#369게임 만들기
def f(n):
    i = 1
    while i <= n:
        if i % 3==0:
            print("짝")
        else:
            print(i)
        i = i+1
        
if __name__=="__main__":
    f(30)

