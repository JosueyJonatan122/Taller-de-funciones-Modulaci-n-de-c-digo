 # ---------- FUNCION PARA PEDIR DATOS ----------
def pedir_empleados():
    num_emp = int(input("Digite la cantidad de empleados: "))
    return num_emp


# ---------- FUNCION PARA CALCULAR NOMINA ----------
def calcular_nomina(num_emp):
    i = 1
    suma_nomina = 0
    resumen = ""

    while i <= num_emp:
        print("Empleado", i)

        horas_trab = float(input("Ingrese horas trabajadas: "))
        pago_hora = float(input("Ingrese valor por hora: "))

        sueldo = horas_trab * pago_hora
        suma_nomina = suma_nomina + sueldo

        resumen = resumen + "Empleado " + str(i) + ": $" + str(sueldo) + "\n"
        i = i + 1

    return suma_nomina, resumen


# ---------- FUNCION PARA MOSTRAR RESULTADOS ----------
def mostrar_nomina(suma_nomina, resumen):
    print("\nNOMINA TOTAL ")
    print(resumen)
    print("Total a pagar en nomina:", suma_nomina)


# ---------- PROGRAMA PRINCIPAL ----------
cantidad = pedir_empleados()
suma_nomina, resumen = calcular_nomina(cantidad)
mostrar_nomina(suma_nomina, resumen)

