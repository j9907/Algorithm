# n,m = map(int,input().split())
# for i in range(n,m+1):
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}')

# 문제
# n = int(input())
# list = list(range(1,n+1))
# x = []
# for i in range(n-1):
#     xa = int(input())
#     x.append(xa)

# for i in x:
#     list.remove(i)

# print(list[0])

# 문제
# n = int(input())
# d = []
# x = 0
# y = 1
# for i in range(n):
#     d.append([])
#     for j in range(n):
#         d[i].append(0)

# d[x][y] = 1
# print(d)
# for i in range(len(d)):
#     for j in range(len(d)):
#         if j == len(d)-1:
#             d[i+1][0]


# n = int(input())
# list = list(map(int,input().split()))

# for i in range(len(list)):
#     print(list[len(list) - i - 1],end=' ')


# n = input()
# print(''.join(reversed(n)))

# 문제
# def solution(numbers):
#     answer = []
#     sum = 0
#     for i in range(1,len(numbers)):
#         for j in range(i):
#             sum = numbers[i] + numbers[j]
#             answer.append(sum)
#     return list(set(sorted(answer)))

# print(solution([1,1,1,1,1]))

n,m = map(int,input().split())
result = 0
for i in range(n):
    x = list(map(int,input().split()))
    min_list = min(x)
    result = max(result,min_list)

print(result)
