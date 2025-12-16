
# ---------- FUNCION PARA PEDIR LA CANTIDAD DE PRODUCTOS ----------
def pedir_cantidad():
    num = int(input("Ingrese la cantidad de productos a registrar: "))
    return num


# ---------- FUNCION PARA CALCULAR LOS VALORES ----------
def calcular_compra(num):
    suma = 0
    detalle = ""

    for i in range(1, num + 1):
        print("Producto", i)
        valor = float(input("Digite el precio del producto: "))
        unidades = int(input("Digite la cantidad: "))

        total_item = valor * unidades
        suma = suma + total_item

        detalle = detalle + "Producto " + str(i) + ": $" + str(total_item) + "\n"

    if suma > 1000:
        rebaja = suma * 0.10
        aviso = "Descuento del 10% aplicado"
    elif suma > 500:
        rebaja = suma * 0.05
        aviso = "Descuento del 5% aplicado"
    else:
        rebaja = 0
        aviso = "No se aplica descuento"

    pago_final = suma - rebaja

    return suma, rebaja, pago_final, aviso, detalle


# ---------- FUNCION PARA MOSTRAR RESULTADOS ----------
def mostrar_info(suma, rebaja, pago_final, aviso, detalle):
    print("\n--- RESUMEN DE COMPRA ---")
    print(detalle)
    print("Subtotal:", suma)
    print("Descuento:", rebaja)
    print("Total a pagar:", pago_final)
    print("Observación:", aviso)


# ---------- PROGRAMA PRINCIPAL ----------
cantidad = pedir_cantidad()
suma, rebaja, pago_final, aviso, detalle = calcular_compra(cantidad)
mostrar_info(suma, rebaja, pago_final, aviso, detalle)
