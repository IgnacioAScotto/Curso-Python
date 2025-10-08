contador = 1
while contador <= 5:
    print(f"Este es el intento numero {contador}.")
    contador += 1

#-----------------------------------------------------------------------------------------------------------
#Pedimos el dato hasta que sea valido.
nombre =""

while nombre =="":
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre =="":
        print("El nombre no puede estar vacio. Intenta de nuevo")
print(f"Hola, {nombre}! Gracias por ingresar tu nombre")
