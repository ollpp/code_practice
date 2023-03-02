import sys

sys.stdin = open('../data/dfs_최대점수구하기.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

print(n, m)

max = 0

def dfs(l, sum, time):
    global max

    if time > m:
        return

    if l == n:
        if sum > max:
            max = sum

    else:
        # 해당 idx 세는 경우
        dfs(l+1, sum+pv[l], time+pt[l])
        # 해당 idx 세지 않는 경우
        dfs(l+1, sum, time)

pv, pt = [], []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    pv.append(a)
    pt.append(b)

dfs(0, 0, 0)
print(max)