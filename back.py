# n 개의 물건
# w 무게 와 , v = 가치
# 첫줄 입력 = n,k
n,k = map(int,input().split())
list = []
list2 = []
sum = 0
for i in range(n):
    w,v = map(int,input().split())
    list.append(w)
    list2.append(v)

for i in range(n):
    for j in range(n):
        if list[i] + list[j] == k:
            sum = list2[i] + list2[j]

print(sum)
