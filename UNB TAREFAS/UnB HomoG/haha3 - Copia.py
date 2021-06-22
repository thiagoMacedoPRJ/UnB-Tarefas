import re

nomes = ['horse_073', 'blue-sky', '96 5 242 93', 'horse_073', 'brown-horse', '36 46 238 195']

pa = []

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
                    result.append(nome)
                else:
                    pass
                    
        if len(result) > 0:
            print('Resultados para "%s":' % (pesquisar))
            
            print(len(result))
                
        else:
            print('Sem ocorrências para "%s".' % (pesquisar))
            
pesquisar(nomes)