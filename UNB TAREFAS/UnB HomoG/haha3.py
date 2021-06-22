import re

nomes = ['horse_073', 'blue-sky', '96 5 242 93', 'horse_073', 'brown-horse', '36 46 238 195']
obj = ['bison','elephant','horse','ibis','sky','mountain','building','flower','sand','tree','field','road','tower','ocean','cliff','waterfall']

pa = []

y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

p = 2

q = 0

def pesquisar(nomes):
    if (len(nomes) < 1):
        print('Não há nomes na lista para pesquisar.')
    else:
        pesquisar = input('Pesquisa:')
        result = []
        for nome in nomes:
            if (pesquisar.lower() in nome.lower()):
                pattern = '^horse'
                res = re.search(pattern, nome)
                if res:
                    result += [nome]
                else:
                    pass
                    
        if len(result) > 0:
            print('Resultados para "%s":' % (pesquisar))
            
            p = obj.index("horse")
                    
            q = len(result)
            print(len(result))
                    
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
            
            result = []
        else:
            print('Sem ocorrências para "%s".' % (pesquisar))
            
pesquisar(nomes)