import sys
from collections import deque

sys.stdin = open('../data/송아지찾기.txt', 'r')

s, e = map(int, sys.stdin.readline().split())

dis = [-1]*(21)

# print(dis)
q = deque()
q.append(s)

dis[s] = 0
while q:
    temp = q.popleft()
    
    for next in (temp-1, temp+1, temp+5):
        if 0<next<21:
            # print(next)
            if dis[next] == -1:
                q.append(next)
                dis[next] = dis[temp] + 1
                
print(dis[e])
