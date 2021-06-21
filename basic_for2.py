# n = int(input())
# list = []
# for i in range(1,n+1):
#     if n % i == 0:
#         list.append(i)

# for i in range(len(list)):
#     print(list[i],end=' ')

#문제
# n = int(input())
# list = []
# for i in range(1,n + 1):
#     if n % i == 0:
#         list.append(i)

# if len(list) == 2:
#     print('prime')
# else:
#     print('not prime')

#문제
# n,m = map(int,input().split())
# print(n**m)

# 문제
# n = int(input())
# sum = 1
# for i in range(n):
#     sum *= n - i
# print(sum)

#문제
# n = int(input())
# m = list(map(int,input().split()))
# sum = len(m) / 2
# c = m[int(sum)]
# print(f'{m[0]} {c} {m[n-1]}')

#  문제
# n,m = map(int,input().split())
# sum = 0
# for i in range(n,m+1):
#     if i % 2 == 0:
#         sum -= i
#         print(f'-{i}',end='')
#     else:
#         sum += i
#         if i == n:
#             print(f'{i}',end='')
#         else:
#             print(f'+{i}',end='')

# print(f'={sum}')

# 주식 구하기
# n = int(input()) # 투자액수
# m = int(input()) # 투자 일수
# sum = n
# map = list(map(int,input().split())) # % 정수 10 = 0.1
# for i in range(len(map)):
#     sum += sum * (map[i] / 100)

# sum = sum - n
# print(f'{sum:.0f}')
# if sum > 0:
#     print('good')
# elif sum == 0:
#     print('same')
# elif sum < 0:
#     print('bad')

# 암호 해독
n = int(input())
list = []
a = 0
b = 0
for i in range(2,n+1):
    if n % i == 0:
        list.append(i)

for i in range(len(list)):
    for j in range(len(list)):
        if(list[i] * list[j] == n):
            a = list[i]
            b = list[j]
            break

if a > b:
    print(f'{b} {a}')
elif b > a:
    print(f'{a} {b}')
elif a == 0 and b == 0:
    print('wrong number')