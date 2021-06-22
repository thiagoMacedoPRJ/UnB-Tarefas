######## Top #########

#print(rabo.count('cuzim'))

y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

p = 2

q = 0

t = True

for i in range(0, q):
    if y[p] > 0: # posição 2 esta ocupada?
        p = p + 2 # sim então você pula 2 casas e verifica se esta casa tambem esta ocupada.
        
        if y[p] > 0:
            pass
        else:
            y[p] = 1
    else: # não?, então coloque nesta casa.
        y[p] = 1
        
print(y)


T, N = map(int, input().split())
input()

r = []
k = []
x = 0

if T == 1:
    for i in range(0, N):
        a = input('')
        if a == '':
            a = input('')
            b = input('')
            c = input('')
            r += [a,b,c]
        else:
            b = input('')
            c = input('')
            r += [a,b,c]
            
print(r)
            
res = r.count('bison'),r.count('elephant'),r.count('horse'),r.count('ibis'),r.count('skr'),r.count('mountain'),r.count('building'),r.count('flower'),r.count('sand'),r.count('tree'),r.count('field'),r.count('road'),r.count('tower'),r.count('ocean'),r.count('cliff'),r.count('waterfall')
for i in range(0,len(res)):
    if res[x] > 0:
        k += [x,res]
        x = x + 1
    else:
        x = x + 1


print(k)