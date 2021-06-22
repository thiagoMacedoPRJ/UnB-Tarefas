import math

T, N = map(int, input().split())

y = []
g = []
x11 = []
x22 = []
y11 = []
y22 = []
grl = []
xy1 = []
w = 0

def soma(l,n):
    if n == 0:
        return l[n];
    else:
        return l[n] + soma(l,n-1)
    
def sub(l,n):
    r = ((n-l)/30)*2
    return round(r)

if T == 1:
    for i in range(0, N):
        a = input('')
        if a == '':
            a = input('')
            b = input('')
            c = input('')
            y += [a,b,c]
        else:
            b = input('')
            c = input('')
            y += [a,b,c]
    for i in range(0,N):
        d = y[w]
        w=w+1
        e = y[w]
        w=w+1
        f = y[w]
        w=w+1
        f = f.replace(" ", ",")
        print(f'{d},{e},{f}')
        
#***************** FIM PARTE 1 *****************#
    
elif T == 2:
    for i in range(0, N):
        a = input('')
        if a == '':
            a = input('')
            b = input('')
            c = input('')
            y += [a,b,c]
        else:
            b = input('')
            c = input('')
            y += [a,b,c]
  
    r = round(y.count('black-bison')*100/N,1),round(y.count('elephant')*100/N,1),round(y.count('white-horse')*100/N,1),round(y.count('brown-horse')*100/N,1),round(y.count('scarlet-ibis')*100/N,1),round(y.count('black-ibis')*100/N,1),round(y.count('white-ibis')*100/N,1),round(y.count('blue-sky')*100/N,1),round(y.count('overcast-sky')*100/N,1),round(y.count('cloudy-sky')*100/N,1),round(y.count('dusthaze-sky')*100/N,1),round(y.count('rocky-mountain')*100/N,1),round(y.count('snowy-mountain')*100/N,1),round(y.count('birdseye-building')*100/N,1),round(y.count('perspective-building')*100/N,1),round(y.count('front-building')*100/N,1),round(y.count('red-flower')*100/N,1),round(y.count('purple-flower')*100/N,1),round(y.count('pink-flower')*100/N,1),round(y.count('sand')*100/N,1),round(y.count('tree')*100/N,1),round(y.count('green-field')*100/N,1),round(y.count('snowy-field')*100/N,1),round(y.count('yellow-field')*100/N,1),round(y.count('road')*100/N,1),round(y.count('tower')*100/N,1),round(y.count('blue-ocean')*100/N,1),round(y.count('green-cliff')*100/N,1),round(y.count('black-cliff')*100/N,1),round(y.count('waterfall')*100/N,1)
    print(f'black-bison: {r[0]}')
    print(f'elephant: {r[1]}')
    print(f'white-horse: {r[2]}')
    print(f'brown-horse: {r[3]}')
    print(f'scarlet-ibis: {r[4]}')
    print(f'black-ibis: {r[5]}')
    print(f'white-ibis: {r[6]}')
    print(f'blue-sky: {r[7]}')
    print(f'overcast-sky: {r[8]}')
    print(f'cloudy-sky: {r[9]}')
    print(f'dusthaze-sky: {r[10]}')
    print(f'rocky-mountain: {r[11]}')
    print(f'snowy-mountain: {r[12]}')
    print(f'birdseye-building: {r[13]}')
    print(f'perspective-building: {r[14]}')
    print(f'front-building: {r[15]}')
    print(f'red-flower: {r[16]}')
    print(f'purple-flower: {r[17]}')
    print(f'pink-flower: {r[18]}')
    print(f'sand: {r[19]}')
    print(f'tree: {r[20]}')
    print(f'green-field: {r[21]}')
    print(f'snowy-field: {r[22]}')
    print(f'yellow-field: {r[23]}')
    print(f'road: {r[24]}')
    print(f'tower: {r[25]}')
    print(f'blue-ocean: {r[26]}')
    print(f'green-cliff: {r[27]}')
    print(f'black-cliff: {r[28]}')
    print(f'waterfall: {r[29]}')
#***************** FIM PARTE 2 *****************#
 
elif T == 3:
    w = 2
    
    for i in range(0, N):
        a = input('')
        if a == '':
            a = input('')
            b = input('')
            c = input('')
            y += [a,b,c]
        else:
            b = input('')
            c = input('')
            y += [a,b,c]
            
    for i in range(0,N):
        d = y[w]
        x1 = int(d.split(' ')[0])
        y1 = int(d.split(' ')[1])
        x2 = int(d.split(' ')[2])
        y2 = int(d.split(' ')[3])
    
        x11.append(x1)
        x22.append(x2)
        y11.append(y1)
        y22.append(y2) 
    
        w=w+3
        
    x1 = soma(x11,N-1)
    x2 = soma(x22,N-1)
    y1 = soma(y11,N-1)
    y2 = soma(y22,N-1)
    print("{} {} {} {}".format(round((x1+x2)/30),round((y1+y2)/30),sub(x1,x2),sub(y1,y2)))


#***************** FIM PARTE 3 *****************#
    
elif T == 4:
    x11 = []
    y11 = []
    xy1 = []
    y22 = []
    grl = []
    g = []


    areaM = 0
    areaM_atributo = 0
    areaM_nome_do_arquivo = 0
    areaME = 65536
    areaME_atributo = 0
    areaME_nome_do_arquivo = 0


    for i in range(0, N):
        espaco = input()
        nome_do_arquivo_1 = input()
        atributo_objeto_1 = input()
        x1, y1, x2, y2 = map(int, input().split())
        
        centro = math.sqrt(128**2 + 128**2)
        centro_atributo = 0
        centro_nome_do_arquivo = 0
        
        if math.sqrt((((y2+y1)/2) - 128)**2 + (((x2+x1)/2) - 128)**2)  < centro:
            centro = math.sqrt((((y2+y1)/2) - 128)**2 + (((x2+x1)/2) - 128)**2)
            centro_atributo = atributo_objeto_1
            centro_nome_do_arquivo = nome_do_arquivo_1
        else:
            centro = centro
            centro_atributo = centro_atributo
            centro_nome_do_arquivo = centro_nome_do_arquivo
        
        
        area = (y2 - y1) * (x2 - x1)
        if area > areaM:
            areaM = area
            areaM_atributo = atributo_objeto_1
            areaM_nome_do_arquivo = nome_do_arquivo_1
        else:
            areaM = areaM
            areaM_atributo = areaM_atributo
            areaM_nome_do_arquivo = areaM_nome_do_arquivo
                    
        if area < areaME:
            areaME = area
            areaME_atributo = atributo_objeto_1
            areaME_nome_do_arquivo = nome_do_arquivo_1
        else:
            areaME = areaME
            areaME_atributo = areaME_atributo
            areaME_nome_do_arquivo = areaME_nome_do_arquivo
        
        x = round((x1+x2)/2)
       
        y = round((y1+y2)/2)
        
        
        grl += [nome_do_arquivo_1,atributo_objeto_1,x,y]
        x11 += [x]
        y11 += [y]
        xy1 += [x,y]
        
        


    for c in range(0,N):
        cent = max(x11)
        centM = min(x11)
        # ------ Centro Acima------
        cima = max(y11)
        cimaM = min(y11)
        # ------ cima bixo Acima------
        geral = max(xy1)
        geralM = min(xy1)
        


    xg = grl.index(cent)

    if xg > 0:
        xg=xg-1
        valx1 = grl[xg]
        xg=xg-1
        valx1m = grl[xg]


    # -_----_- Encima e o valor esquerdo _-----_--
    xgm = grl.index(centM)

    if xgm > 0:
        xgm=xgm-1
        valM = grl[xgm]
        xgm=xgm-1
        valxm = grl[xgm]
    # -_----_- Encima e o valor Direito _-----_--

    yg = grl.index(cima)

    if yg > 0:
        yg=yg-2
        valy = grl[yg]
        yg=yg-1
        vay = grl[yg]
    # -_----_- Encima e o valor cima _-----_--

    ygm = grl.index(cimaM)

    if ygm > 0:
        ygm=ygm-2
        valyM = grl[ygm]
        ygm=ygm-1
        vaM = grl[ygm]
    # -_----_- Encima e o valor cimaB _-----_--


    mai = grl.index(geral)

    if mai > 0:
        mai=mai-2
        maior = grl[mai]
        mai=mai-1
        maior2 = grl[mai]




    men = grl.index(geralM)

    if men > 0:
        men=men-2
        menor = grl[men]
        men=men-1
        menor2 = grl[men]





    print(f'mais central: {centro_atributo},{centro_nome_do_arquivo}')

    print(f'mais a esquerda: {valM},{valxm}')
    print(f'mais a direita: {valx1},{valx1m}')
    print(f'mais acima: {valyM},{vaM}')
    print(f'mais abaixo: {valy},{vay}')

    print(f'maior area: {areaM_atributo},{areaM_nome_do_arquivo}')
    print(f'menor area: {areaME_atributo},{areaME_nome_do_arquivo}')

#***************** FIM PARTE 4 *****************#
else:
    for i in range(0, N):
        a = input()
        if a == '':
            a = input()
            b = input()
            c = input()
            y += [a,b,c]
        else:
            b = input()
            c = input()
            y += [a,b,c]
    
    r = y.index('tree')
    
    if r > 0:
        r=r-1
        l = y[r]
        conf = y.index(l)
        conf=conf+1
        if conf == 'green-field' or 'snowy-field' or 'yellow-field':
            print('nada ')
        else:
            print(l)