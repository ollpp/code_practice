from collections import deque
import sys

sys.stdin = open("../input_data/12.오큰수.txt", 'r')

n = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

# index를 저장
mydeque = deque()

# mydeque에 저장된 index를 통해 값 비교 및 정답list에 추가
answer = [0] * len(n_list)

for i in range(n):
    while mydeque and n_list[mydeque[-1]] < n_list[i]:
        answer[mydeque[-1]] = n_list[i]
        mydeque.pop()

    mydeque.append(i)

while mydeque:
    answer[mydeque[0]] = -1
    mydeque.popleft()


for i in answer:
    print(i, end=' ')
# print(answer)