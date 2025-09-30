'''Para este ejercicio necesitamos un software que ayude a registrar y calcular información
Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes.

Tu tarea para esta semana es la siguiente:

1. Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. 
    Validar que los ingresos sean números positivos. Si se ingresa un valor negativo,
    mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

2. Calcular el total acumulado durante los 6 meses y el promedio mensual.
    Mostrá este resultado al final del programa. '''


nombre = input('Nombre: ').strip().title()
apellido = input('Apellido: ').strip().title()
correo = input('Correo electronico: ').strip()

#validacion basica del correo electronico
if '@' not in correo or correo.count("@") != 1 or " " in correo:
    print("Correo inválido. Terminando el programa")
else:
    print(f"\nRegistro de ingresos para {nombre} {apellido} ({correo})")

ingresos = []
total = 0
mes = 1

while mes <= 6:
    ingreso_texto = input(f'Ingreso del mes {mes}: $')
    if ingreso_texto.isdigit():
        ingreso = int(ingreso_texto)
        if ingreso > 0:
            ingresos.append(ingreso)
            total += ingreso
            mes += 1

        else:
            print("No se aceptan valores negativos.")

    else:
        print("Ingresa un numero valido.")


    #Mostramos el resumen con while
    print('\n--- Resumen Financiero ---')
    indice = 0
    while indice < len(ingresos):
        print(f'Mes {indice + 1}: ${ingresos[indice]}')
        indice += 1

    print(f'Total acumulado en 6 meses: ${total}')
    print(f"Promedio mensual: ${total // 6}")