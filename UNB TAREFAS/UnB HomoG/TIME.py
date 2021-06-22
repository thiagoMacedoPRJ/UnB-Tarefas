k = int(input())
N = list(map(int, input().split()))

a = 0
b = 1
o = []
c = 0
t = True

while t:
  if N[a] == N[b]:
    a = a + 2
    b = b + 2
    o += [a]
    c = c + 1
    if c == 5:
        t = False
    else:
        pass
  else:
    print('{} sozinho'.format(N[a]))
    t = False


if a == k:
  print('tudo certo')
else:
  pass