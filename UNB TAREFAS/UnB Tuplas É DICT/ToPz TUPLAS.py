a = input()

l = []
y = {}
z = {}
for i in range(0,len(a)):
    x = a[i]
    o = a.count(x)
    y[x] = o

print(y)