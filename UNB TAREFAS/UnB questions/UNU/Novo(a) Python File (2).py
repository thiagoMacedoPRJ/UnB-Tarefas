a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

# primeiro
ab = a // 360
a = a - ab*360


m = a // 30
a = a - m*30

d = a



# segundo
an = b // 360
b = b - an*360

me = b // 30
b = b - me*30

di = b



# terceiro
ano = c // 360
c = c - ano*360

mes = c // 30
c = c - mes*30

dia = c

print('{} ano(s) {} mes(es) {} dia(s)'.format(ab ,m, d))
print('{} ano(s) {} mes(es) {} dia(s)'.format(an ,me, di))
print('{} ano(s) {} mes(es) {} dia(s)'.format(ano ,mes, dia))