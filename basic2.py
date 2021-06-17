#문제 5
n,m,p = map(int,input().split())
if m < 10:
    if p < 10:
        print(f'{n}0{m}00{p}')
    elif p < 100:
        print(f'{n}0{m}0{p}')
    else:
        print(f'{n}0{m}{p}')
else:
    if p < 10:
        print(f'{n}{m}00{p}')
    elif p < 100:
        print(f'{n}{m}0{p}')
    else:
        print(f'{n}{m}{p}')