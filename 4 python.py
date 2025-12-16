def ingresar_lote():
    cantidad = int(input("Ingrese el número de unidades del lote: "))
    return cantidad


def revisar_lote(cantidad):
    i = 1
    malas = 0
    detalle_defectos = ""
    detalle_buenas = ""

    while i <= cantidad:
        print("Unidad", i)
        estado = input("Ingrese D si es defectuosa u O si está en buen estado: ")

        if estado == "D" or estado == "d":
            malas += 1
            detalle_defectos += "Unidad " + str(i) + " defectuosa\n"
        else:
            detalle_buenas += "Unidad " + str(i) + " correcta\n"

        i += 1

    porcentaje = (malas / cantidad) * 100
    return malas, porcentaje, detalle_defectos, detalle_buenas


def mostrar_informe(cantidad, malas, porcentaje, defectos, buenas):
    print("\nINFORME DEL LOTE")
    print("Total de unidades:", cantidad)
    print("Unidades defectuosas:", malas)
    print("Porcentaje de defectos:", porcentaje)

    print("\nDetalle de defectuosas:")
    print(defectos)

    print("Detalle de unidades correctas:")
    print(buenas)


# programa principal
total_unidades = ingresar_lote()
defectuosas, porc, lista_defectos, lista_buenas = revisar_lote(total_unidades)
mostrar_informe(total_unidades, defectuosas, porc, lista_defectos, lista_buenas)
