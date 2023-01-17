import sys
from collections import deque


sys.stdin = open('../input_data/46.특정거리의도시찾기.txt', 'r')

n, m, l, s = map(int, sys.stdin.readline().split())

visited = [-1] * (n+1)
q = deque()
road = [[] for _ in range(n+1)]

for _ in range(m):
    sa, v = map(int, sys.stdin.readline().split())
    road[sa].append(v)

# print(road)

def bfs(s):
    q.append(s)
    visited[s] += 1
    while q:
        tmp = q.popleft()
        for node in road[tmp]:
            if visited[node] == -1:
                visited[node] = visited[tmp] + 1
                q.append(node)


bfs(s)

answer = []
for i in visited:
    if i == l:
        answer.append(i)
# print(s)
# print('l',l)
# print('visited : ', visited)
# print('answer',answer)
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)