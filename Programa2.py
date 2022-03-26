#4.1 Implementar una tupla de un solo elemento

print ("Prática número 2, Sabrina Colmenarez")

print (" ")

tupla = ('Esto es una tupla')

print (tupla)


print ("---------------------------------------------------------------------")

#4.2 Dada la lista de edades sobre una población que se ha ido a vacunar
#Elimine de la lista todas las ocurrencias del entero 10

vEdades = [2,7,58,7,45,26,10,8,56,57,97,19,11,53,3,99,
          62,78,29,937,42,56,86,28,86,95,26,49,67,21,
          815,67,10,58,512,24,92,89,67,53,10,9,83,1,
          44,10,77,98,73,57]

print ("Las edades son", vEdades)

print (" ")

vEdades.remove(10)
vEdades.remove(10)
vEdades.remove(10)
vEdades.remove(10)

print ("Las edades son todas estas menos el número 10", vEdades)
