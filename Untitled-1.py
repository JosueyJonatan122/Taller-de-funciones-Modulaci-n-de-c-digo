def capturar_datos():
    calificacion = float(input("Digite la calificación del 1 al 5 del servicio (0 para terminar): "))
    return calificacion


def procesar(acum, cont_excelentes, calificacion):
    acum = acum + calificacion

    if calificacion == 5:
        cont_excelentes = cont_excelentes + 1

    return acum, cont_excelentes


def operacion(acum, total_pedidos, cont_excelentes):
    if total_pedidos > 0:
        promedio = acum / total_pedidos
    else:
        promedio = 0

    print("Total de pedidos procesados:", total_pedidos)
    print("Puntuación total acumulada:", acum)
    print("Promedio general de satisfacción:", promedio)
    print("Pedidos excelentes (5 estrellas):", cont_excelentes)


# ------------ PROGRAMA PRINCIPAL -------------

total_pedidos = int(input("¿Cuántos pedidos va a calificar como máximo?: "))

acum = 0
cont_excelentes = 0
cont_real = 0

for i in range(total_pedidos):
    calificacion = capturar_datos()

    if calificacion == 0:
        break

    cont_real += 1
    acum, cont_excelentes = procesar(acum, cont_excelentes, calificacion)

operacion(acum, cont_real, cont_excelentes)
