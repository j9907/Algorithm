# 문제 15
# n,m,p = map(int,input().split())
# list = [n,m,p]
# sum = 0
# for i in range(len(list)):
#     r = max(list)
#     sum += list[i]
    

# if sum - r > r:
#     print('yes')
# else:
#     print('no')

# 문제 16
# n,m = map(int,input().split())
# if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
#     if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#         print('31')
#     elif m == 2:
#         print('29')
#     else:
#         print('30')
# else:
#     if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#         print('31')
#     elif m == 2:
#         print('28')
#     else:
#         print('30')

# 문제 17
# n = 홍보를 하지않을 경우 수입
# m = 홍보를 할 경우의 수입
# p = 홍보 비용
# n,m,p = map(int,input().split())
# a = m - p # 홍보를 할 경우 이익
# if a > n:
#     print('advertise')
# elif a < 0 or a < n:
#     print('do not advertise')
# else:
#     print('does not matter')

# 문제 18
# n,m,p = map(int,input().split())
# if n + m > p:
#     if n == m == p:
#         print('정삼각형')
#     elif n == m or m == p or n == p:
#         print('이등변삼각형')
#     elif n**2 + m**2 == p**2:
#         print('직각삼각형')
#     else:
#         print('삼각형') 
# else:
#     print('삼각형아님')

# 문제 19
# n = 경기타임
# m,p = 스코어
n,m,p = map(int,input().split())
count = 0
while n < 90:
    # 5분마다 골
    # 투입 시 바로 골
    if n % 5 == 0:
       m += 1
    
    n += 1

if m > p:
    print('win')
elif m < p:
    print('lose')
else:
    print('same')
