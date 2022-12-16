import sys
from collections import deque
# sys.stdin = open("/Users/seokhwan/Library/CloudStorage/OneDrive-개인/sh/03. code_test/code_practice/input_data/10.find_min.txt", 'r')
sys.stdin = open("../input_data/10.find_min.txt", 'r')


n, l = map(int, sys.stdin.readline().split())
detail = []
mydeque = deque()

detail = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    # 만약 mydeque 가 없다면 (첫번째 인덱스라면)
    while mydeque and mydeque[-1][1] > detail[i]:
        mydeque.pop()

    mydeque.append((i, detail[i]))
    if mydeque[0][0] <= i-l:
        mydeque.popleft()        

    print(mydeque[0][1], end=' ')

# mydeque.append((1, 1)
