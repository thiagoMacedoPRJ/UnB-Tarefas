n1, n2, n3 = input().split()
p1, p2, p3 = input().split()

p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

media = ((n1*p1)+(n2*p2)+(n3*p3)) / (p1+p2+p3)

print('{:.6f}'.format(media))
