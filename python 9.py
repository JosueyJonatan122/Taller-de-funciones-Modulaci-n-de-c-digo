
def pedir_venta():
    cantidad= int(input("Ingrese la cantidad vendida hoy: "))
    return cantidad


# ---------- FUNCION PARA CONTROLAR EL INVENTARIO ----------
def revisar_inventario():
    stock= 50
    minimo= 10
    texto= ""
    dia= 0

    while True:
        venta= pedir_venta()
        dia= dia + 1

        stock= stock - venta
        texto= texto + "Dia " + str(dia) + ": se vendieron " + str(venta) + " unidades, stock = " + str(stock) + "\n"

        if stock<= minimo:
            texto= texto + "Se debe reponer el producto\n"
            break

    return stock, texto, dia


# ---------- FUNCION PARA MOSTRAR RESULTADOS ----------
def mostrar_control(stock, texto, dia):
    print("\nCONTROL DE INVENTARIO")
    print("Dias registrados:", dia)
    print("Stock final:", stock)
    print("\nDetalle de ventas:")
    print(texto)

stock, texto, dia = revisar_inventario()
mostrar_control(stock, texto, dia)
