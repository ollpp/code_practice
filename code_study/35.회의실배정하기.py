import sys

sys.stdin = open('../input_data/35.회의실배정하기.txt', 'r')

n = int(sys.stdin.readline())

a = [[0]*2 for _ in range(n)]

# print(a)
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    
    a[i][0] = e
    a[i][1] = s

print(a)

a.sort()

print(a)

end = -1
cnt = 0
for i in range(n):
    if a[i][1] >= end:
        cnt += 1
        end = a[i][0]

print(cnt)