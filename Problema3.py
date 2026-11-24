# Fase 5 - Evaluación Final POA
# Problema 3 - Reabastecimiento de inventario
# Estudiante: [Ashly Sophia Cañas Delgado]

# Función para calcular la cantidad a solicitar
def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Matriz de inventario
inventario = [
    ["A001", "Teclado", 5, 10],
    ["A002", "Ratón", 20, 15],
    ["A003", "Monitor", 3, 8],
    ["A004", "Audífonos", 10, 10],
    ["A005", "Memoria USB", 2, 14]
]


# Encabezado del programa
print("========================================")
print("REABASTECIMIENTO DE INVENTARIO")
print("========================================")

# Recorrido de la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamada a la función
    cantidad = calcular_reabastecimiento(
        stock_actual, stock_minimo
    )

    # Mostrar los resultados
    print("Artículo:", nombre)
    print("Cantidad a solicitar:", cantidad)
    print("----------------------------------------")

print("Fin del informe de inventario.")