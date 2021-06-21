# n,m = input().split()
# a,b = input().split()
# c,d = input().split()
# sum = (float(n) * int(m)) + (float(a) * int(b)) + (float(c) * int(d))
# print(f'{sum:.1f}')

# 문제
# a,b,c,d = map(int,input().split())

# if a / b > c / d:
#     print('>')
# elif a / b == c / d:
#     print('=')
# elif a / b < c/ d :
#     print('<')

# 로또
a,b,c,d,e,f,g = map(int,input().split())
lotto1 = [a,b,c,d,e,f]
h,i,j,k,l,m = map(int,input().split())
lotto2 = [h,i,j,k,l,m]
count = 0
check = 0

for i in range(len(lotto1)):
    for j in range(len(lotto2)):
        if lotto1[i] == lotto2[j]:
            count+= 1
            continue

if count == 6:
    print('1')
elif count == 5:
    for i in range(len(lotto2)):
        if lotto2[i] == g:
            check = 1
            break
        else:
            check = 2
elif count == 4:
    print('4')
elif count == 3:
    print('5')
else:
    print('0')


if check == 1:
    print('2')
elif check == 2:
    print('3')
