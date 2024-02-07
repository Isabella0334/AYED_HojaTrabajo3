#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTORES:
#           ISABELLA RECINOS RODRÍGUEZ / 23003
#   FECHA DE INICIO: MARTES 30 DE ENERO DEL AÑO 2024
#   FECHA DE ENTREGA: MARTES 06 DE FEBRERO DEL AÑO 2024
#   DESCRIPCIÓN: Shell Sort
#---------------------------------------------------------------------
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        interval //= 2
    return array