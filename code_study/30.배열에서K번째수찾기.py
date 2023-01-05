import sys

sys.stdin = open('../input_data/30.배열에서K번째수찾기.txt', 'r')

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# print(n,m)

start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, n+1):
        temp += min(mid//i, n)

    if temp >= k:
        answer = mid
        end = mid - 1

    else :
        start = mid + 1

print(answer)