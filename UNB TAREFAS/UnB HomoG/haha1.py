import re

nomes = ['horse_047','horse_047','horse_047','brown-horse','blue-sky']
cu = []


obj = ['bison','elephant','horse','ibis','sky','mountain','building','flower','sand','tree','field','road','tower','ocean','cliff','waterfall']

j = 0


def pesquisa(j,nomes):
    if (len(nomes) < 1):
        print('Não há nomes na lista para pesquisar.')
    else:
        pesquisar = obj[j]
        result = []
            
            
        for nome in nomes:
            if (pesquisar.lower() in nome.lower()):
                result.append(nome)
            
            
            if len(result) > 0:
                print('Resultados para "%s":' % (pesquisar))
            
                cu.append(len(result))
                
                print(cu)
                
                j = j + 1
                if j == 15:
                    print('ok')
                else:
                    return pesquisa(j,nomes)
            
            else:
                print('Sem ocorrências para "%s".' % (pesquisar))
                j = j + 1
                if j == 15:
                    print('ok')
                else:
                    return pesquisa(j,nomes)
        
pesquisa(j,nomes)