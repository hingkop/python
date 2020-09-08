#소수판별
def f(n):
    i = 2
    while i < n:
        if n%i==0:
            break
        i = i+1 
        
    if i==n:
        print("소수") 
    else:
        print("합성수")