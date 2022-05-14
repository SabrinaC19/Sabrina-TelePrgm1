print ("------------PROGRAMA DE SABRINA COLMENAREZ SECCIÓN 1---------------\n")

#-------------------variables--------------------

cadena_1= 'Prueba centrado en python\n'

tamaño_c=(len(cadena_1))

 #----------------- FUNCIONES-----------------------------

 #---------------Funcion Circulo--------------------------

def area_circulo ():

    radio= float(input("Ingrese el rádio de su circulo: "))

    return (3.1415*(radio**2))


#--------------Funcion Numero mayor-----------------------

def numero_mayor (): 

    numero_a= int(input("Ingrese el primer numero: "))

    numero_b= int(input("\nIngrese el segundo numero: "))

    numero_c= int(input("\nIngrese el tercer numero: "))

    if numero_b < numero_a > numero_c:
        n_mayor= numero_a

    elif numero_a < numero_b > numero_c:
        n_mayor= numero_b

    elif numero_a < numero_c > numero_b:
         n_mayor= numero_c

    elif numero_a== numero_b and numero_a> numero_c:
        n_mayor= numero_a

    elif numero_a== numero_c and numero_a> numero_b:
        n_mayor= numero_a

    elif numero_b== numero_c and numero_b> numero_a:
        n_mayor= numero_b

    else:
        n_mayor= "Ninguno porque son iguales"

    return (n_mayor)


#--------------------3.Función impares------------------------

def numeros_impares ():

    lista= [1,2,3,4,5,6,7,8,9,10]
    
    n_impares=[]

    suma= 0

    print("\nLa lista de enteros es ", lista)
    
    for n in lista:
        if n % 2!= 0:
            n_impares.append(n)

    print ("\nLa lista de impares es:", n_impares)

    for n in n_impares:

        suma+= n

    n_impares= suma

    return n_impares


#----------------4.Función de Cadena Centrada------------------

def cadena (cadena_1,tamaño_c):

    print ("\n",cadena_1)

    print ("La cantidad de caracteres que tiene la cadena es: ", tamaño_c)

    cadena_2= cadena_1.rjust(tamaño_c+tamaño_c)

    return cadena_2

#--------------------- Menu -----------------------------------
menu_principal= int(input (
"1- Calcular Área de un Circulo\n"
"2- Máximo de tres valores\n"
"3- Lista y suma de impares\n"
"4- Cadena centrada\n"
"5- Salir\n"
"\n->"))

while menu_principal != 5:

    if menu_principal == 1:
        area= area_circulo()
        print (f"\nEl area es: {area}\n")

    elif menu_principal == 2:
        n_mayor= numero_mayor()
        print (f"\nEl numero mayor es: {n_mayor}\n")

    elif menu_principal == 3:
        n_impares= numeros_impares()
        print ("\nLa sumatoria de los impares es: ", n_impares, "\n")

    elif menu_principal == 4:
        cadena_centrada= cadena (cadena_1,tamaño_c)
        print ("\n",cadena_centrada)

    else:
        print("Ingrese alguno de los números indicados")

    menu_principal= int(input (
    "1- Calcular Área de un Circulo\n"
    "2- Máximo de tres valores\n"
    "3- Lista y suma de impares\n"
    "4- Cadena centrada\n"
    "5- Salir\n"
    "\n->"))



        
