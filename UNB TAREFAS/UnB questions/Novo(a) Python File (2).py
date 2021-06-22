a = int(input())
b = int(input())
p = int(input())

total = a/b
resu = f'%.{p}f' % total

print('O resultado de {} por {} é {}.'.format(a,b,resu))
