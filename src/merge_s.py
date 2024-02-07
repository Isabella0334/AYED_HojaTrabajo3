#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTORES:
#           ISABELLA RECINOS RODRÍGUEZ / 23003
#   FECHA DE INICIO: MARTES 30 DE ENERO DEL AÑO 2024
#   FECHA DE ENTREGA: MARTES 06 DE FEBRERO DEL AÑO 2024
#   DESCRIPCIÓN: Merge Sort
#---------------------------------------------------------------------
def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array