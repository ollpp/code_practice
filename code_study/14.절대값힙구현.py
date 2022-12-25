from queue import PriorityQueue
import sys

input = sys.stdin.readline
sys.stdin = open('../input_data/14.절대값 힙 구현.txt', 'r')


# N = int(input())
N = int(sys.stdin.readline())

print(N)
print(type(N))

my_q = PriorityQueue()

for i in range(N):
    req = int(sys.stdin.readline())

    if req != 0:
        my_q.put((abs(req), req))
    
    else :
        if my_q.empty() :
            print('0')
        
        else : 
            temp = my_q.get()
            str_temp = str(temp[1])
            print(f'{str_temp}')