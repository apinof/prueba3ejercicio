from funciones1 import(grabar, buscar, listar, salir)
import os
import time
import numpy as np
e=0 
base=[]
try:
    while e==0:
        os.system('cls')
        opcion=int(input('''Seleccione una de las siguientes opciones:

(1) Grabar
(2) Buscar
(3) Listar
(4) Salir
'''))
        if opcion==1: #--------- menú opcion 1
                base.append(grabar())
        elif opcion==2: #--------- menú opcion 2
                buscarrut=input('Ingrese el rut a buscar\n')
                buscar(buscarrut,base)
                opcion1=int(input('''
                
Desea Volver al menu Principal?
(1) SI
(2) NO\n'''))
                if opcion1==1:
                    e=0
                elif opcion1==2:
                    e=1
                else:
                    print('Opción no válida')    
        elif opcion==3: #--------- menú opcion 3
                listar(base)
                opcion1=int(input('''

Desea Volver al menu Principal?
(1) SI
(2) NO\n'''))
        elif opcion==4: #--------- menú opcion 4
            e=salir()
except:
    print('opcion no válida')
