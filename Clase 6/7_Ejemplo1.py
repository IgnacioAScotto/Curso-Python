# Ingresos Mensuales:
ingresos = [40000, 55000, 60000, 45000, 70000, 50000]
count = 0

for ingreso in ingresos:
    if ingreso > 50000:
        count += 1
print(f"Cantidad de ingresos superiores a $50.000: {count}")