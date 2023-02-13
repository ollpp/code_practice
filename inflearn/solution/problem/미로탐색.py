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

cnt = 0

def DFS(x, y):
    global cnt

    if x==6 and y==6:
        cnt+=1


    for i in range(4):
        
        after_x = x+dx[i]
        after_y = y+dy[i]

        if 0<=after_x<=6 and 0<=after_y<=6 and board_list[after_x][after_y]==0:
            board_list[after_x][after_y] = 1
            DFS(after_x, after_y)
            board_list[after_x][after_y] = 0


board_list[0][0] = 1
DFS(0, 0)
print(board_list[0][0])
print(cnt)

for i in range(7):
    print(board_list[i])