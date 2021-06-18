#문제 5
# n,m,p = map(int,input().split())
# if m < 10:
#     if p < 10:
#         print(f'{n}0{m}00{p}')
#     elif p < 100:
#         print(f'{n}0{m}0{p}')
#     else:
#         print(f'{n}0{m}{p}')
# else:
#     if p < 10:
#         print(f'{n}{m}00{p}')
#     elif p < 100:
#         print(f'{n}{m}0{p}')
#     else:
#         print(f'{n}{m}{p}')

# 문제6
# h,m = map(int,input().split())

# m = h*60+m
# m -= 30
# h = m//60
# m %= 60
# h %= 24
# print(f'{h} {m}')

# 문제 7
n = int(input())
n2 = n % 10
n1 = n // 10
sum = str(n2) + str(n1)
result = int(sum) * 2
if result > 100:
        result -= 100
        if result <= 50:
            print(result)
            print("GOOD")
        else:
            print(result)
            print("OH MY GOD")
        
else:
    if result <= 50:
            print(result)
            print("GOOD")
    else:
            print(result)
            print("OH MY GOD")
