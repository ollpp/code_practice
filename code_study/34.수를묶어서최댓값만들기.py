from queue import PriorityQueue
import sys

sys.stdin = open('../input_data/34.수를묶어서최댓값만들기.txt', 'r')

n = int(sys.stdin.readline())

plus_q = PriorityQueue()
minus_q = PriorityQueue()
one = 0
zero = 0

for i in range(n):
    temp = int(sys.stdin.readline())

    if temp > 0 :
        # 양수 내림차순 정렬을 위해 -1 을 곱해준다.
        plus_q.put(i* (-1)) 
    
    elif temp == 0 :
        zero += 1
    
    elif temp == 1:
        one += 1
    
    else : 
        minus_q.put(i)

sum = 0

while plus_q.qsize() > 1:
    tmp1 = plus_q.get() * (-1)
    tmp2 = plus_q.get() * (-1)
    sum += tmp1 * tmp2

while minus_q.qsize() > 1:
    tmp1 = minus_q.get()
    tmp1 = minus_q.get()
    sum += tmp1 * tmp2

# while one >= 0 :
#     sum += 1
#     one -= 1

sum += one

if minus_q.qsize() == 1 & zero > 0:
    minus_q.get()

print(sum)