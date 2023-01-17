import sys
from collections import deque

sys.stdin = open('../input_data/47.효율적으로해킹하기.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

answer = [0] * (n+1)
q = deque()
a = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    a[s].append(e)

def bfs(x):
    q.append(x)
    while q:
        tmp = q.popleft()
        for item in a[tmp]:
            answer[item] += 1
            q.append(item)

for i in range(1, n+1):
    visited = [False] * (n+1)
    bfs(i)

maxVal = -1

for i in answer:
    maxVal = max(maxVal, i)

for i in range(len(answer)):
    if maxVal == answer[i]:
        print(i, end = ' ')

