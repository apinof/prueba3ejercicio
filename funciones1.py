import os
import time
import numpy as np

def grabar():
    c=1
    d=1
    while c==1:
        os.system('cls')
        rut=input('Ingrese su rut (ej 12345678-9), si termina en k favor ingresar con minúscula\n')    
        rut1=list(rut)
        rut1.remove('-')
        dv=rut1[-1]
        rut1.pop()
        for i in range(len(rut1)):
            rut1[i] = int(rut1[i])
        rut2=rut1
        rut2.reverse()
        a=1
        for i in range(len(rut2)):
            if a<7:
                a=a+1
            else:
                a=2
            rut2[i]=rut2[i]*a
            b=0
        for i in range(len(rut2)):
            b=b+rut2[i]
        b=b%11
        final=11-b
        if final==10:
            final='k'
        elif final==11:
            final=0
        final=str(final)
        if final==dv:
            resultadodv=1
        else:
            resultadodv=0

        if resultadodv==1:
            c=0
        else:
            os.system('cls')
            print('Rut incorrecto')
            time.sleep (1)
    os.system('cls')
    nombre=input('Ingrese su nombre completo\n')
    os.system('cls')
    edad=int(input('Ingrese su edad\n'))
    if edad>=18:
        os.system('cls')
        print('Usted es mayor de edada, puede continuar')
    else:
        os.system('cls')
        print('Usted no es mayor de edad, no es posible ingresarlo a la base de datos.')
        time.sleep(2)
        d=0
    if d==1:
        os.system('cls')
        estado_civil=input('Ingrese su estado civil, (C = Casado, S = Soltero, V = Viudo).\n')
        os.system('cls')
        fec_afiliacion=input('ingrese la fecha de afiliacion\n')
        dato=[rut,nombre,edad,estado_civil,fec_afiliacion]
    return(dato)

def buscar(buscarrut,base):
        basea=np.array(base)  
        for i in range(len(base)):
            if basea[i][0]==buscarrut:
                os.system('cls')
                print(f''' 
Rut:............. {basea[i,0]}
Nombre:...........{basea[i,1]}
Edad:.............{basea[i,2]}
Estado Civil:.....{basea[i,3]}
fecha aficiacion: {basea[i,4]}''')
                
def listar(base):
    nficha=0
    baseb=np.array(base)  
    os.system('cls')
    for i in range(len(base)):
        if baseb[i][3]=='s':
            nficha=nficha+1
            print(f''' --- ficha {nficha} ---
Rut:............. {baseb[i,0]}
Nombre:...........{baseb[i,1]}
Edad:.............{baseb[i,2]}
Estado Civil:.....{baseb[i,3]}
fecha aficiacion: {baseb[i,4]}''')

def salir():
    os.system('cls')
    opcion2=int(input('''Seguro que desea sali?
(1) SI
(2) NO\n'''))
    if opcion2==1:
        os.system('cls')
        print('Esta saliendo del programa, adiós.')
        time.sleep(2)
        salida=1
    elif opcion2==2:
        print('Volviendo al menú principal')
        time.sleep(2)
    else:
        print('Opción no válida')        
    os.system('cls')
    return(salida)


    



