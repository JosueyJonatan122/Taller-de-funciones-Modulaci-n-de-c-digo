def pedir_transaccion():
    opcion = input("Ingrese operación (d=deposito, r=retiro, fin=salir): ")
    valor = 0
    if opcion != "fin":
        valor = int(input("Ingrese el valor: "))
    return opcion, valor


def procesar_transaccion(opcion, valor, saldo_actual, total_movimientos):
    mensaje = ""

    if opcion == "d":
        saldo_actual += valor
        total_movimientos += 1
        mensaje = "Depósito realizado"

    elif opcion == "r":
        if valor <= saldo_actual:
            saldo_actual -= valor
            total_movimientos += 1
            mensaje = "Retiro realizado"
        else:
            mensaje = "Fondos insuficientes"

    return saldo_actual, total_movimientos, mensaje


def mostrar_resumen(saldo, movimientos, mensaje):
    print(mensaje)
    print("Saldo actual:", saldo)
    print("Cantidad de movimientos:", movimientos)
    print("--------------------------")


saldo = 1500
movimientos = 0

while True:
    tipo, monto = pedir_transaccion()
    if tipo == "fin":
        break
    saldo, movimientos, texto = procesar_transaccion(tipo, monto, saldo, movimientos)
    mostrar_resumen(saldo, movimientos, texto)
