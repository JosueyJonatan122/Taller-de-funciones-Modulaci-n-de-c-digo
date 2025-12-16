def pedir_horas():
    horas= int(input("Ingrese las horas extra,numero negativo para terminar: "))
    return horas

def calcular_bonos():
    total= 0
    cantidad_empleados = 0

    while True:
        horas= pedir_horas()

        if horas < 0:
            break

        if horas > 5:
            bono= horas * 15
        else:
            bono= horas * 10

        total = total + bono
        cantidad_empleados = cantidad_empleados + 1

        print("Bono del empleado:", bono)

    return total, cantidad_empleados

def mostrar_bonos(total, cantidad_empleados):
    print("\nRESULTADOS")
    print("Empleados con bono:", cantidad_empleados)
    print("Total pagado en bonos:", total)

total, cantidad_empleados = calcular_bonos()
mostrar_bonos(total, cantidad_empleados)
