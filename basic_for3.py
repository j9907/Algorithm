# n = int(input())

# for i in range(1,10):
#     sum = i * n
#     print('*' * sum)

# 문제
# list=[]
# for i in range(3):
#     n,m = map(int,input().split())
#     list.append(n*m)

# print(max(list))

# 문제 = 약수 n 을 제외한
# n,m,p = map(int,input().split())
# count = 0
# result = 0
# cont = 0
# for i in range(1,n):
#     if n % i == 0:
#         count += 1
#print(count)

# 문제 = 최대공약수
n,m,p = map(int,input().split())
list = [n,m,p]
max = max(list)
count = 0

for i in range(1,max+1):
    if n % i == 0 and m % i == 0 and p % i == 0:
        count = i

print(count)