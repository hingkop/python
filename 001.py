#반복문 활용해 0-n 합 구하기
def sum_to_n(n):
    i = 0
    sum = 0
    while ( i<= n):
        sum = sum + i
        i = i+1
    print (sum)

if __name__ == '__main__':
    sum_to_n(100)
