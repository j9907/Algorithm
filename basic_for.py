# a,b = map(int,input().split())

# if a >= b:
#     for i in range(b,a+1):
#         print(i,end=' ')
# elif b >= a:
#     for i in range(a,b+1):
#         print(i,end=' ')

#문제2
# a,b = input().split()
# oa = ord(a)
# ob = ord(b)
# for i in range(oa,ob+1):
#     print(chr(i),end=' ')

#문제 3
# a,b,c,d,e,f,g,h,i,j = map(int,input().split())
# list = [a,b,c,d,e,f,g,h,i,j]
# count = 0

# for i in range(len(list)):
#     if list[i] % 5 == 0:
#         count = list[i]
#         break

# print(count)

# 문제 4
# n,m = map(int,input().split())
# for i in range(n,m+1):
#     if i % 2 != 0:
#         print(i,end=' ')

#문제 5,6
# n = int(input())
# sum = 0
# # for i in range(1,n+1):
# #     sum += i
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum += i
# print(sum)

#문제 7
# n,m = map(int,input().split())
# sum = 0
# for i in range(n,m+1):
#     if i % 3 == 0:
#         sum += i
    
# print(sum)

#문제 8
# n = int(input())

# for i in range(1,10):
#     print(f'{n}*{i}={n*i}')

#문제9
n = int(input())
sum = 0
for i in range(n):
    a = map(int,input().split())
    sum += a[i]

print(sum)