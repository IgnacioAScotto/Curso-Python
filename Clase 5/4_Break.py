intentos = 0
max_intentos = 3
nombre = ""
while intentos < max_intentos and nombre == "":
   nombre = input("Ingresá tu nombre de usuario: ").strip()
   if nombre == "":
       print("El nombre no puede estar vacío. Intentá de nuevo.")
       intentos += 1
if nombre != "":
   print(f"Bienvenido/a, {nombre}!")
else:
   print("Se agotaron los intentos. Intente más tarde.")