import sys
from collections import deque

sys.stdin = open('../data/계단오르기.txt', 'r')

n = int(sys.stdin.readline())

s_list = [0] * (n+1)

s_list[1] = 1
s_list[2] = 2

for i in range(3, n+1):
    s_list[i] = s_list[i-1] + s_list[i-2]

print(s_list)