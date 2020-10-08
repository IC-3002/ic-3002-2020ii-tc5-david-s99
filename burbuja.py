
def burbuja_optimizado(A):
    i=ordenado = verifica_ordenado(A)
    while i < len(A) and verifica_ordenado(A)==False:
        i = i+1
        if verifica_ordenado(A)==True:
            return A
        else:
            j=0
            while j < len(A) -1:
                if A[j] > A[j+1]:
                    if verifica_ordenado(A):
                        return A
                    else:
                        temp = A[j]
                        A[j] = A[j+1]
                        A[j+1] = temp
                j+=1
    return A
                
    
    
def  verifica_ordenado(A):
    i=0
    while i < (len(A)-1):
        if A[i]<=A[i+1]:
            i+=1
        else:
            return False
    return True
