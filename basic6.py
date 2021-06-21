# #비만도측정1,2
# n,m = map(float,input().split())
# weight = 0
# # weight = (n - 100) * 0.9 측정 1
# if n < 150:
#     weight = n - 100
# elif n >= 150 and n < 160:
#     weight = (n - 150) / 2 + 50
# else:
#     weight = (n - 100) * 0.9

# condition_factor = (m - weight) * 100 / weight

# if condition_factor <= 10:
#     print('정상')
# elif condition_factor > 10 and condition_factor <= 20:
#     print('과체중')
# else :
#     print('비만')

# 터널통과하기2
# a,b,c = map(int,input().split())
# if a > 170:
#     if b > 170:
#         if c > 170:
#             print('PASS')
#         else:
#             print(f"CRASH {c}")
#     else:
#         print(f'CRASH {b}')
# else:
#     print(f'CRASH {a}')
