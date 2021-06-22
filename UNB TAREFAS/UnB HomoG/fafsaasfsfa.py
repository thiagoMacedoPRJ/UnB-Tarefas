k = 0
j = ['abacaba','programa']
def cu(j,k):
    if k == 5:
        print('é')
    else:
        k = k + 1
        return cu(j,k)
        
cu(j,k)