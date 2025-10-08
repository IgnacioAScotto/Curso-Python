productos = ["P001", "P002", "P003", "P004", "P005"]
producto_a_buscar = "P003"
for producto in productos:
    if producto == producto_a_buscar:
        print("Producto encontrado:", producto)
        break
    print("Buscando...")
print("Fin de la búsqueda.")
