import sys

sys.stdin = open('../input_data/25.친구관계파악하기.txt', 'r')

n, m = map(int, sys.stdin.readline().split())

fr_list = [[] for _ in range(n+1)]
arrive = False
visited = [False]*(n+1)

for _ in range(m):
    f, s = map(int, sys.stdin.readline().split())
    fr_list[f].append(s)
    fr_list[s].append(f)


def dfs(idx, depth):
    global arrive
    if depth == 5:
        arrive = True
        return 

    visited[idx] = True
    
    for i in fr_list[idx]:
        if visited[i] == False:
            dfs(i, depth+1)

    visited[idx] = False
    
    # 방문여부를 True로 하고 해당 idx 방문했을 경우 dfs 진행
    # 해당 idx 방문안한경우로 추가 진행
    # 끝나는 부분에 돌려주는 이유는
    # n개의 loop 안에서 dfs를 돌릴때
    # 해당 visited 리스트를 공유하기 때문


for i in range(n):
    dfs(i, 1)
    if arrive:
        break


if arrive:
    print(1)
else:
    print(0)