y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

a = 'horse_073'


if a == 'horse_073':
    y[2] = 1
else:
    y.append(a) 

b = 'horse_073'

if b == 'horse_073':
    if y[2] == 1:
        y[4] = 1
    else:
        y[2] = 1

strg = [str(y) for y in y]

strg = "".join(strg)

print('{}{}'.format(b,strg.replace("", " ",16)))