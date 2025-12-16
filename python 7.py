# ---------- FUNCION PARA PEDIR LA CANTIDAD ----------
def pedir_estudiantes():
    cant = int(input("Ingrese la cantidad de estudiantes: "))
    return cant


# ---------- FUNCION PARA CALCULAR PROMEDIO ----------
def calcular_promedio(cant):
    total_notas = 0
    listado = ""

    for i in range(1, cant + 1):
        print("Estudiante", i)
        nota = float(input("Digite la nota: "))

        total_notas = total_notas + nota
        listado = listado + "Estudiante " + str(i) + ": " + str(nota) + "\n"

    promedio = total_notas / cant
    return promedio, listado


# ---------- FUNCION PARA MOSTRAR RESULTADOS ----------
def mostrar_datos(promedio, listado):
    print("\n--- RESULTADOS ---")
    print("Notas ingresadas:")
    print(listado)
    print("Promedio final:", promedio)


# ---------- PROGRAMA PRINCIPAL ----------
cantidad = pedir_estudiantes()
promedio, listado = calcular_promedio(cantidad)
mostrar_datos(promedio, listado)
