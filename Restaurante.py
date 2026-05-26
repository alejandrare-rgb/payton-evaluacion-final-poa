# =============================================
# SISTEMA DE PEDIDOS - RESTAURANTE
# =============================================

# Matriz:
# [Código, Nombre, Categoría, Precio]

menu = [
    [1, "Hamburguesa Especial", "Comida", 18000],
    [2, "Pizza Familiar", "Comida", 30000],
    [3, "Perro Caliente", "Comida", 15000],
    [4, "Jugo Natural", "Bebida", 8000],
    [5, "Gaseosa", "Bebida", 5000],
    [6, "Helado", "Postre", 10000]
]

categoria_objetivo = "Comida"
umbral = 20000
descuento = 0.15


# Función para calcular precio final
def calcular_precio(categoria, precio):

    if categoria == categoria_objetivo and precio > umbral:

        precio_final = precio - (precio * descuento)

    else:
        precio_final = precio

    return precio_final


# Mostrar menú
print("\n====== MENÚ DEL RESTAURANTE ======\n")

for producto in menu:

    print(
        producto[0], "-",
        producto[1],
        "|", producto[2],
        "| $", producto[3]
    )

pedido = []
total = 0

while True:

    opcion = int(input("\nIngrese el código del producto: "))

    encontrado = False

    for producto in menu:

        if opcion == producto[0]:

            nombre = producto[1]
            categoria = producto[2]
            precio = producto[3]

            precio_final = calcular_precio(
                categoria,
                precio
            )

            pedido.append([nombre, precio_final])

            total += precio_final

            print("\nProducto agregado")

            print("Nombre:", nombre)

            print("Precio final: $", precio_final)

            encontrado = True

    if encontrado == False:
        print("Producto no existe")

    continuar = input(
        "\n¿Desea agregar otro producto? (si/no): "
    )

    if continuar.lower() != "si":
        break


print("\n========== FACTURA ==========")

for producto in pedido:

    print(producto[0], "- $", producto[1])

print("\nTOTAL A PAGAR: $", total)

print("\nGracias por su compra")