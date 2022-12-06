import sys
sys.stdin = open("/Users/seokhwan/Library/CloudStorage/OneDrive-개인/sh/03. code_test/code_practice/input_data/DP_가장 큰 정사각형.txt", 'r')

n, m = map(int, input().split())


# 입력받은 정사각형의 정보를 넣어줄 list : arr
arr = [] 
# 최대 정사각형의 크기를 저장할 배열 : dp
dp = [[0]*m for _ in range(n)]

# arr 배열에 입력받는 값 초기화
for _ in range(n):
    arr.append(list(map(int, list(input()))))

# 최대값
rslt = 0

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
            # dp[i-1][j-1], dp[i][j-1], dp[i-1][j]가 모두 정사각형 오른쪽 아래라면 +1 이 될것이고
            # 그렇지 않으면 최대값이 갱신되지 않을것이다
            # 즉, 세가지 경우가 모두 정사각형일 경우만
            # 최대값 rslt가 갱신된다고 가정한 점화식이다.
        else :
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        
        breakpoint()
        rslt = max(rslt, dp[i][j])

print(rslt*rslt)    

