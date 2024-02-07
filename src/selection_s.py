#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTORES:
#           ISABELLA RECINOS RODRÍGUEZ / 23003
#   FECHA DE INICIO: MARTES 30 DE ENERO DEL AÑO 2024
#   FECHA DE ENTREGA: MARTES 06 DE FEBRERO DEL AÑO 2024
#   DESCRIPCIÓN: Selection Sort
#---------------------------------------------------------------------
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    return array