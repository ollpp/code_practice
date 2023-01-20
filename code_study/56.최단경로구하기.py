import sys
from queue import PriorityQueue

sys.stdin = open('../input_data/56.최단경로구하기.txt', 'r')

n , v = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

# distance (거리)
d = [10000] * (n+1)

# 방문여부
visited = [False] * (n+1)

# 입력받을 행렬
info = [[] for _ in range(v+1)]



# 우선순위 큐 (BFS를 진행하기 위해)
q = PriorityQueue()

for _ in range(v):
    node1, node2, w = map(int, sys.stdin.readline().split())

    info[node1].append((node2, w))


q.put((0, k))
d[k] = 0

while q.qsize() > 0:
    current = q.get()
    cu_v = current[1]

    if visited[cu_v]:
        continue

    visited[cu_v] = True

    for a in info[cu_v]:

        item = a[0]
        length = a[1]


        if d[item] > d[cu_v] + length:
            d[item] = d[cu_v] + length
            q.put((d[item], item))

print(d)

for i in range(1, n+1):
    if visited[i]:
        print(d[i])
    else:
        print('INF')