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
# n = int(input())
# a = list(map(int,input().split()))
# count = 0
# for i in range(n):
#     if a[i] % 2 == 0:
#         count += 1

# print(count)


# a = [int(a) for a in input().split()]
#문제 10
# a = 시작값 , b = 곱할값 , c = 더할값, n = 몇항인지
# a,b,c,n = map(int,input().split())
# sum = int(a)
# for i in range(1,int(n)):
#         sum = sum * int(b) + int(c)

# print(sum)

# 문제11
# n = int(input())
# count = 0
# for i in range(1,n+1):
#     if i % 10 == 1:
#         count += 1

# print(count)

# n = int(input())
# x = list(map(int,input().split()))
# print(max(x))

n,m = map(int,input().split())
# 홀수 = i
# 짝수 = i * 10
# n,m = 리스트의 n값
# list = []
# a = 1
# if n > m:
#     for i in range(n):
#         b = int(a) * 10
#         list.append(int(a))
#         list.append(int(b))
#         a += 1
# else:
#     for i in range(m):
#         b = int(a) * 10
#         list.append(int(a))
#         list.append(int(b))
#         a += 1
# print(list[n-1] + list[m-1])


   