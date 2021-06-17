#문제1
# n = int(input())
# hour = 0
# min = 0

# while True:
#     if n >= 60 :
#         n = n - 60
#         hour += 1
#         continue
#     else:
#         break

# print(f'{hour} {n}')

# 문제2
# n = int(input())
# 온도 = 9 / 5 * n + 32
# print(f'{온도:.3f}')

# 문제 3
# n = int(input())
# sum = 2012 - n + 1
# if sum < 2000:
#     sum  -= 1900
#     print(f'{sum} 1')
# else:
#     sum -= 2000
#     print(f'{sum} 3')

#문제4
n,m,p = map(int,input().split())
if p < 10:
    print(f'{n}{m}0{p}')
else:
    print(f'{n}{m}{p}')
