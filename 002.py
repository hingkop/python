#재귀 사용해 1-20 호출
def print_to_n(n):
    if n > 0 :
        print_to_n(n-1)
    print(n)

if __name__ == '__main__':
    print_to_n(20)