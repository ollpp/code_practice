from collections import deque
import sys

sys.stdin = open('../input_data/27.미로탐색하기.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

input_mat = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    numbers = list(sys.stdin.readline())
    for j in range(m):
        input_mat[i][j] = int(numbers[j])

print(input_mat)

def bfs(x, y):

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        now = q.popleft()

        for i in range(4):
            x = now[0] + dx[i]
            y = now[1] + dy[i]

            if x >= 0 and y >= 0 and x < n and y < m:
                if input_mat[x][y] != 0 and not visited[x][y]:
                    q.append((x, y))
                    visited[x][y] = True
                    input_mat[x][y] = input_mat[now[0]][now[1]] + 1

bfs(0, 0)
print(input_mat[n-1][m-1])