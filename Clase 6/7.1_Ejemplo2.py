usuarios = ["Ana", "Luis", "Andrés", "María", "Alejandro", "Lucía"]
letra_buscada = "A"

for nombre in usuarios:
    if nombre.startswith(letra_buscada):
        print(f"Nombre que empieza con con '{letra_buscada}': {nombre}")