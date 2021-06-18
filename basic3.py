# n = int(input())

# if n > 0:
#     print("양수")
# elif n < 0:
#     print("음수")
# elif n == 0:
#     print('0')

# 문제 8
# n = int(input())

# if n >= 90:
#     print("A")
# elif n >= 80:
#     print("B")
# elif n >= 70:
#     print("C")
# elif n>= 60:
#     print("D")
# else:
#     print('F')

# 문제 9
# n = int(input())

# if n <= 10:
#     print('정상')
# elif n <= 20:
#     print('과체중')
# else:
#     print('비만')

# 문제 10
# n = int(input())
# if n == 11 or n == 12 or n == 13:
#     print(f'{n}th')
# elif n % 10 == 1:
#     print(f'{n}st')
# elif n % 10 == 2:
#     print(f'{n}nd')
# elif n % 10 == 3:
#     print(f'{n}rd')
# else:
#     print(f'{n}th')

# 문제 11
# n,m = map(float,input().split())
# list = [n+m,m+n,n-m,m-n,n*m,m*n,m//n,n//m,n**m,m**n]
# print(f'{max(list):.6f}')

#문제 12
# n,m = map(int,input().split())
# if m % n == 0:
#     nu = m // n
#     sum = n * nu
#     print(f'{n}*{nu}={sum}') 
# elif n % m == 0:
#     nu = n // m
#     sum = m * nu
#     print(f'{m}*{nu}={sum}')
# else:
#     print('none')

# 문제 13
# o,t,th,f = map(int,input().split())
# sum = o + t + th + f
# if sum == 0:
#     print('모')
# elif sum == 1:
#     print('도')
# elif sum == 2:
#     print('개')
# elif sum == 3:
#     print('걸')
# else:
#     print('윷')

# 문제 14
n,m = map(int,input().split())
sum = 0
list = [400,340,170,100,70]

sum += list[n-1]
sum += list[m-1]

if sum > 500:
    print('angry')
else:
    print('no angry')

    
