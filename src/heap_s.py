#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTORES:
#           ISABELLA RECINOS RODRÍGUEZ / 23003
#   FECHA DE INICIO: MARTES 30 DE ENERO DEL AÑO 2024
#   FECHA DE ENTREGA: MARTES 06 DE FEBRERO DEL AÑO 2024
#   DESCRIPCIÓN: Heap Sort
#---------------------------------------------------------------------
def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r

      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr):
      n = len(arr)
      for i in range(n//2, -1, -1):
          heapify(arr, n, i)
      for i in range(n-1, 0, -1):
          # Intercambia valores
          arr[i], arr[0] = arr[0], arr[i]
          heapify(arr, i, 0)
      return arr