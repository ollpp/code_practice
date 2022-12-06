import sys
sys.stdin = open("../input_data/bfs_바이러스.txt", 'r')
#이 아래쪽에 maps 변수 선언

n = int(input())

input_list = list(map(int, input().split()))

d = [0]*n
d[0] = input_list[0]
d[1] = input_list[1]
for i in range(2,len(d)):
    d[i] = max(d[i-1], d[i-2]+input_list[i])

print(d[i])