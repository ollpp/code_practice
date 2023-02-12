import sys

sys.stdin = open('./data/section6_순열.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

chk = [0] * (n+1)
ans = [0] * m


cnt = 0
def dfs(x):
    global cnt
    if x == m:
        for i in range(x):
            print(ans[i], end=' ')  
            cnt += 1  
        print()
    
    else: 
        for i in range(1, n+1):
            if chk[i] == 0:
                chk[i] = 1
                ans[x] = i
                dfs(x+1)
                chk[i] = 0

dfs(0)
    