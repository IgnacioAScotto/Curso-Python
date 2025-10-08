# range(inicio, fin, paso)

#Inicio: Numero donde comienza la secuencia (opcional, por defecto 0)
#Fin: Numero donde termina la secuencia (no incluido)
#Paso: Intervalo entre numeros (porcional, por defecto 1)

#ejemplo 1:
for i in range(5):
    print(i)

print("--------------------------------------------------------------------------------------")
#ejemplo 2: Valor de inicio especifico 
for i in range (3, 7):
    print(i)

print("--------------------------------------------------------------------------------------")
#ejemplo 3: el parametro paso a paso
for i in range(0, 10, 2):
    print(i)

print("--------------------------------------------------------------------------------------")
#ejemplo 4: secuencias decrecientes 
for i in range(10, 0, -2):
    print(i)

print("--------------------------------------------------------------------------------------")
#ejemplo 5: recorrer listas con range()
frutas = ["manzana", "banana", "naranja"]
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}")