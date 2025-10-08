'''Para este ejercicio necesitamos un software que ayude a registrar y calcular información
Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros y nuestras clientes.

Tu tarea para esta semana es la siguiente:

1. Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. 
    Validar que los ingresos sean números positivos. Si se ingresa un valor negativo,
    mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

2. Calcular el total acumulado durante los 6 meses y el promedio mensual.
    Mostrá este resultado al final del programa. '''

mes = 1
total = 0

while mes <= 6:
    ingreso = int(input(f"Ingresa tu sueldo del mes {mes}: $"))
    if ingreso < 0:
        print("El numero es negativo. Intenta de nuevo.")
        continue
    total += ingreso
    mes += 1

print(f"Tus ingresos fueron: ${total}")


