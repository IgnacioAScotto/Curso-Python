texto = "Hola, mundo"
print(texto.replace ("mundo", "Python"))

#texto = "Hola"
#print(texto[0]="J")  # Esto generará un error porque las cadenas son inmutables

ingreso = 60000

edad = 25

if ingreso < 50000:

    print("Ingresos bajos.")

elif edad < 30:

    print("Joven con buenos ingresos.")

else:

    print("Adulto con buenos ingresos.")

#-------------------------------------------------------------------------------------------------------

nombre = "Ana"

saludo = f"Hola, {nombre}!"

print(saludo)

#-------------------------------------------------------------------------------------------------------
match 10:

    case 5:

        print("Cinco.")

    case 10:

        print("Diez.")

    case _:

        print("Otro número.")

#-------------------------------------------------------------------------------------------------------
edad = int(input("Ingresá tu edad: "))

if edad < 18:

    print("Sos menor de edad.")

else:

    print("Sos mayor de edad.")

#-------------------------------------------------------------------------------------------------------
texto = "Python"

if "P" in texto and texto.endswith("on"):

    print("Condición cumplida.")

else:

    print("Condición no cumplida.")

#-------------------------------------------------------------------------------------------------------
dia = input("Ingresá un día de la semana: ")

match dia:

    case "Lunes":

        print("Inicio de semana.")

    case "Viernes":

        print("Fin de semana.")

    case _:

        print("Día intermedio.")