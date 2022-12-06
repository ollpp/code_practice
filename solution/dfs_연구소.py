import sys
sys.stdin = open("/Users/seokhwan/Library/CloudStorage/OneDrive-개인/sh/03. code_test/code_practice/input_data/dfs_연구소.txt", 'r')

# 안전 영역 count 함수
# virus를 퍼뜨리는 함수
# 울타리를 세우는 함수

n, m = map(int, input().split())

data = []
temp = [[0]*m for _ in range(n)]


for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# return 할 안전영역의 개수
result = 0

# virus를 퍼뜨리는 함수 
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny]=2
                virus(nx, ny)

# 안전영역 count 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
    return score

# 울타리를 세우는 모든 경우
def dfs(count):
    global result

    # 울타리가 3개인 경우
    # 탈출부
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 바이러스 퍼뜨리기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 최신화된 현 상황 count
        result = max(result, get_score())
        return
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)