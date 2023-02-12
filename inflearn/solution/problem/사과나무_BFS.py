import sys
from collections import deque

sys.stdin = open('../data/사과나무_BFS.txt', 'r')

n = int(sys.stdin.readline())

chk = [[0]*n for _ in range(n)]
apple_list = []

for i in range(n):
    apple_list.append(list(map(int, sys.stdin.readline().split())))

print(apple_list)
print(chk)

s = n//2
chk[s][s] = 1
q = deque()
q.append((s, s))
L = 0
cnt = apple_list[s][s]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

while True:
    if L == s:
        break
    size = len(q)
    for k in range(size):
        print(k)
        tmp = q.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]

            if chk[x][y] != 1:
                cnt += apple_list[x][y]
                chk[x][y] = 1
                    
                q.append((x, y))

    for x in chk:
        print(x)
    L += 1 

print(cnt)

print(3 + 18 + 28 + 78 + 16)

print(chk)
    
