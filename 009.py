#소수 호출
def check (n):
    i = 2
    while i < n :
        if n % i == 0:
            break
        i = i + 1
     
    if i == n :
        print(n) 
        print("은 소수")
    else :
        print(n) 
        print("합성수")


if __name__=="__main__":
    check(2)
    check(3)
    check(4)
    check(5)

        
    
    

