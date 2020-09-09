#소수판별
def f(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i+1 
    if i==n:
        print("소수") 
    else:
        print("합성수")

f(19) 
f(130)
f(37)
f(20)
f(21)



