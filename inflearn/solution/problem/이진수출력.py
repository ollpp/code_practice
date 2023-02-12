import sys

sys.stdin = open('../data/이진수출력.txt', 'r')

def DFS(x):
    if x == 0:
        return
    DFS(x//2)
    print(x%2, end = ' ')

DFS(11)
