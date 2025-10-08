# En este ejemplo vamos a pedirle al usuario que sume numeros positivos. Si ingresa un numero negativo, usamos el continue para saltarlo y pedir otro.
numero = 0
print("Ingresa numeros positvos para sumarlos. Ingresa 0 para terminar.")
suma = 0
while True:
    #solicitamos al usuario un numero.
    numero = int(input("Ingresa un numero: "))
    #verificamos si el numero es negativo.
    if numero < 0:
        print("El numero es negativo, se ignorara. Intenta de nuevo.")
        continue
    if numero == 0:
        break

    suma += numero
print(f"La suma de los numeros positivos es: {suma}")