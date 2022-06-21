n = int(input())
input_list = list(map(int, input().split()))

d = [0]*n
d[0] = input_list[0]
d[1] = input_list[1]
for i in range(2,len(d)):
    d[i] = max(d[i-1], d[i-2]+input_list[i])

print(d[i])