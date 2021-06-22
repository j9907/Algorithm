# n = input()
# list = []
# sum = 0
# for i in range(len(n)):
#     list.append(int(n) % 10)
#     n = int(n) // 10
# for i in range(len(list)):
#     sum += list[i]

# if sum % 7 == 4:
#     print('suspect')
# else:
#     print('citizen')

# 문제
# n = int(input())
# list = list(map(int,input().split()))
# print(f'{max(list)} {min(list)}')

#문제
# 철망의 길이 = n 
# n = int(input())
# sum = n / 4
# print(f'{int(sum**2)}')

# 문제
n = int(input())
widest = 0
bend = 0

for i in range(1, int(n/2)):
    if widest < i * (n - i*2):
        widest = i * (n - i*2)
        bend = i

print(bend)