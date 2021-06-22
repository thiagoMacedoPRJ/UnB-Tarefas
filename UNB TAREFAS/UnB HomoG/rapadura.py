'''
a = int(input())

b=a-1
print(f'Termo: {b}')
print('Quantidades:')

if a == 0:
    b = a+1
    print(f'fibonacci({a}) - {b}')
    b = b-1
else:
    b=b-1

for i in range(0,a+1):
    print(f'fibonacci({i}) - {b}')
    b=b+1
    if b >= 4:
        b=b-1
    else:
        b=b+1
'''
L = [1,2,3] 
def soma_aninhada(L):
    L.remove(']')
    L = sum(L)
    return L
    
print(soma_aninhada([[1,2,3]]))
