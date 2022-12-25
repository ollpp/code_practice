import sys

sys.stdin = open('../input_data/24.신기한소수찾기.txt', 'r')

n = int(sys.stdin.readline())

# print(n)

# 소수찾는 함수
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    # print('hi2')
    return True

def dfs(x):
    # print('hi')
    if len(str(x)) == n:
        print(x)
    
    else:
        # print('hi3')
        for i in range(1,10):
            if i % 2 == 0:
                # print('hi4')
                continue           
            else:
                if isPrime(10*x + i):
                    # print('hi6')
                    dfs(10*x + i)


# for i in range(2, 5):
#     print(i)
print(n)
dfs(2)
dfs(3)
dfs(5)
dfs(7)