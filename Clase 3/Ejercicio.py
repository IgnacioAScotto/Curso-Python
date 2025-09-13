# Solicitar datos del usuario
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad_texto = input("Edad: ")
correo = input("Correo electrónico: ")

edad = int(edad_texto)
# Verificamos que los campos no estén vacíos
# Y que la edad ingresada sea un número mayor a 18
if nombre !='':
  if apellido !="":
    if correo !='':
      if edad_texto.isdigit():
        if edad>=18:
          print("\n--- Datos del cliente ---")
          print("Nombre:", nombre)
          print("Apellido:", apellido)
          print("Edad:", edad)
          print("Correo:", correo)
        else:
          print("ERROR: La edad debe ser mayor a 18.")
      else:
        print("ERROR: La edad debe ser un numero")
    else:
      print("ERROR: El correo no puede estar vacío.")
  else:
    print("ERROR: El apellido no puede estar vacío.")
else:
  print("ERROR: El nombre no puede estar vacío.")