import sys
from collections import deque

sys.stdin = open('../data/미로의최단거리통로.txt', 'r')

board_list = [0]*7
l_list = [[0]*7 for _ in range(7)]

for i in range(7):
    board_list[i] = list(map(int, sys.stdin.readline().split()))

print(board_list)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = deque()
q.append((0, 0))
cnt = 0
while q:
    temp = q.popleft()
    
    for i in range(4):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]

        # print(x)
        if 0<=x<=6 and 0<=y<=6 and board_list[x][y] == 0:
            board_list[x][y] = 1
            l_list[x][y] = l_list[temp[0]][temp[1]] + 1
            q.append((x, y))
            if x == 6 and y == 6:
                cnt +=1 

if l_list[6][6] != 0:
    print(l_list[6][6])
else:
    print(-1)

print(cnt)