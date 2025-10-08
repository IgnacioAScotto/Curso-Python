#En este ejemplo, utilizamos un contador para limitar la cantidad de intentos que tiene la persona para ingresar su nombre de usuario.

#Inicializamos el contador en 0
intentos = 0
#Estabecle el maximo de itentos permitidos
max_intentos = 3
#Usamos un bucle que se detendra si el usuario ingresa un nombre invalido o agota los intentos 
while intentos < max_intentos:
    #Solicitamos al usuario que ingrese su nombre
    nombre = input("Ingresa tu nombre de usuario: ").strip()

    #Verificamos si el nombre ingresado no esta vacia
    if nombre != "":
        print(f"Bienvenido/a {nombre}") #Mensaje de extio

        break #salimos del bucle si se ingresa un nombre valido    
    
    else:
        print("El nombre no puede estar vacio. Intenta de nuevo")
        #incrementamos el contador de intentos 
        intentos += 1

        #verificamos si se agotaron los intentos
        if intentos == max_intentos:
            print("Se agotaron los intentos. Intente de nuevo mas tarde")
    