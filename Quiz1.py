#두번째 수
# n,m,p = map(int,input().split())

# list = [n,m,p]
# list.sort()
# print(list[1])

# 나이계산1

y,s = input().split()
age = y[0:2]
age = int(age)
sum = 0
if int(s) == 1 or int(s) == 2:
    age += 1900
else:
    age += 2000

sum = 2012 - age

print(sum + 1)