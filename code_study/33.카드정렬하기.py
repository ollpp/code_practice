from queue import PriorityQueue
import sys

sys.stdin = open('../input_data/33.카드정렬하기.txt', 'r')

n = int(sys.stdin.readline())

myq = PriorityQueue()

for _ in range(n):
    myq.put(int(sys.stdin.readline()))

cnt = 0

while myq.qsize()>1:
    data1 = myq.get()
    data2 = myq.get()

    temp = data1 + data2
    myq.put(temp)
    cnt += temp


print(cnt)