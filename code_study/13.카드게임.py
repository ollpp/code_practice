from collections import deque
import sys

sys.stdin = open('../input_data/13.카드게임.txt', 'r')


n = int(sys.stdin.readline())

card = deque()dfdf

for i in range(n):
    card.append(6-i)


while len(card) > 1:
    card.pop()
    temp = card.pop()
    card.appendleft(temp)

ans = card.pop()

print(ans)