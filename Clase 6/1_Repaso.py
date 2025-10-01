# Estructura ciclica while imprimiendo del 1 al 3

contador = 1

while contador <= 3:
    print(contador)
    contador = contador + 1

print("Terminado")


#Estructura repetitiva For

#Instruccion for
for i in range(1,4,1):
    print(i)

print("Terminado")

#el while y el for en este caso hacen lo mismo

#lista

num = 4

nombre = "Sebastian"

nombres = ["Juan", "Leonardo", "Mara"]

print(nombres[0])
print(nombres[1])
print(nombres[2])

#para que imprima todos automaticamente.
for i in range(0,3,1):
    print(nombres[i])

#indica cuantos nombres tiene la lista
print(len(nombres))

#para que por mas que se modifique la lista, siempre imrpima todos los nombres.
for i in range(0,len(nombres),1):
    print(nombres[i])

#La instruccion ciclica se usa para repetir instrucciones de acuerdo a una condicion establecida.

productos = ["manzanas", "piñas", "bananas", "uvas"]

for producto in productos:
    print("Producto disponible:", producto)


