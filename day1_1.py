# 문제
n = int(input())
d = [0 for i in range(23)]
for i in range(10):
    n = map(int,input().split())
    d[n] += 1
print(d)