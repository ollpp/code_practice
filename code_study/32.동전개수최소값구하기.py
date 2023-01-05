import sys

sys.stdin = open('../input_data/32.동전개수최소값구하기.txt', 'r')

n, k = map(int, sys.stdin.readline().split())

print(n, k)
a = [0]*n
print(a)
cnt = 0

for i in range(n):
    a[i] = int(sys.stdin.readline())

for i in range(n-1, -1, -1):
    if k >= a[i]:
        cnt += (k // a[i])
        k = k % a[i]

print(cnt)