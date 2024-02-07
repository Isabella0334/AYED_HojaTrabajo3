#---------------------------------------------------------------------
#   UNIVERSIDAD DEL VALLE DE GUATEMALA  
#   DEPARTAMENTO DE CIENCIAS DE LA COMPUTACIÓN
#   CC2016 - 20
#   AUTORES:
#           ISABELLA RECINOS RODRÍGUEZ / 23003
#   FECHA DE INICIO: MARTES 30 DE ENERO DEL AÑO 2024
#   FECHA DE ENTREGA: MARTES 06 DE FEBRERO DEL AÑO 2024
#   DESCRIPCIÓN: Comparación de Sorts
#---------------------------------------------------------------------
from gnome_s import gnome_sort
from merge_s import mergeSort
from quick_s import quickSort
from radix_s import radixSort
from selection_s import selectionSort
from shell_s import shellSort
from heap_s import heapSort
from tkinter import messagebox
import os
import random
from random import randrange
import time
import sys

sys.setrecursionlimit(1500) 

ventana = True

while ventana == True:
    print("***** Menú *****")
    print("Selecciona que tipo de arreglo deseas utilizar para hacer prueba de los sorts y ordenarlo de forma ascendente")
    print("1. Arreglo de 10 elementos")
    print("2. Arreglo de 1000 elementos")
    print("3. Arreglo de 3000 elementos")
    print("4. Arreglo de 10 elementos en forma descendente")
    print("5. Arreglo de 1000 elementos en forma descendente")
    print("6. Arreglo de 3000 elementos en forma descendente")
    print("7. Salir")

    try:
        num = int(input("Elección: "))
    except:
        messagebox.showerror("Error","Valor inválido")
    else:
        if num >= 1 and num <= 6:
            if num == 1:
                arr = [0]*10
                for i in range(10):
                    arr[i] = random.randrange(0, 10000)
            elif num == 2:
                arr = [0]*1000
                for i in range(1000):
                    arr[i] = random.randrange(0, 10000)
            elif num == 3:
                arr = [0]*3000
                for i in range(3000):
                    arr[i] = random.randrange(0, 10000)
            elif num == 4:
                arr = [0]*10
                for i in range(10):
                    arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif num == 5:
                arr = [0]*1000
                for i in range(1000):
                    arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif num == 6:
                arr = [0]*3000
                for i in range(3000):
                    arr[i] = random.randrange(0, 10000)
                arr.sort(reverse = True)
            elif num == 7:
                ventana = False

            with open('values.txt', 'w') as f:
                for item in arr:
                    f.write("%s\n" % item)
        else:
            messagebox.showerror("Error","Opción inválida")
#   Uso de IA "Python os: How to save an array to a text file and read ir as an array?"
        read_list = []
        with open('values.txt', 'r') as f:
            for line in f:
                read_list.append(int(line.strip()))
        
        # Gnome Sort
        st = time.perf_counter()
        gs_list = gnome_sort(read_list)
        et = time.perf_counter()

        print("Gnome Sort")
        #print("  Lista ordenada: "+str(gs_list))
        print("  Tiempo: "+str(et - st)+" s \n")

        # Merge Sort
        st = time.perf_counter()
        ms_list = mergeSort(read_list)
        et = time.perf_counter()

        print("Merge Sort")
        #print("  Lista ordenada: "+str(ms_list))
        print("  Tiempo: "+str(et - st)+" s \n")

        # Quick Sort
        st = time.perf_counter()
        qs_list = quickSort(read_list, 0, int(len(read_list)-1))
        et = time.perf_counter()

        print("Quick Sort")
        #print("  Lista ordenada: "+str(qs_list))
        print("  Tiempo: "+str(et - st)+" s \n")

         # Radix Sort
        st = time.perf_counter()
        rs_list = radixSort(read_list)
        et = time.perf_counter()

        print("Radix Sort")
        #print("  Lista ordenada: "+str(rs_list))
        print("  Tiempo: "+str(et - st)+" s \n")

         # Selection Sort
        st = time.perf_counter()
        ss_list = selectionSort(read_list, int(len(read_list)))
        et = time.perf_counter()

        print("Selection Sort")
        #print("  Lista ordenada: "+str(ss_list))
        print("  Tiempo: "+str(et - st)+" s \n")

         # Shell Sort
        st = time.perf_counter()
        shs_list = shellSort(read_list, int(len(read_list)))
        et = time.perf_counter()

        print("Shell Sort")
        #print("  Lista ordenada: "+str(shs_list))
        print("  Tiempo: "+str(et - st)+" s \n")

         # Heap Sort
        st = time.perf_counter()
        hs_list = heapSort(read_list)
        et = time.perf_counter()

        print("Heap Sort")
        #print("  Lista ordenada: "+str(hs_list))
        print("  Tiempo: "+str(et - st)+" s \n")