
def pedir_edad():
    edad = int(input("Ingrese la edad,0 para terminar: "))
    return edad


# ---------- FUNCION PARA PROCESAR ENCUESTA ----------
def procesar_datos():
    suma = 0
    contador = 0
    objetivo = 0
    texto = ""

    while True:
        edad = pedir_edad()

        if edad == 0:
            break

        contador = contador + 1
        suma = suma + edad
        texto = texto + "Edad ingresada: " + str(edad) + "\n"

        if edad >= 25 and edad <= 45:
            objetivo = objetivo + 1

    if contador > 0:
        promedio = suma / contador
    else:
        promedio = 0

    return objetivo, promedio, texto, contador


# ---------- FUNCION PARA MOSTRAR RESULTADOS ----------
def mostrar_encuesta(objetivo, promedio, texto, contador):
    print("\nRESULTADOS DE LA ENCUESTA")
    print("Total de personas:", contador)
    print("Personas entre 25 y 45 años:", objetivo)
    print("Edad promedio:", promedio)
    print("\nListado de edades:")
    print(texto)


# ---------- PROGRAMA PRINCIPAL ----------
objetivo, promedio, texto, contador = procesar_datos()
mostrar_encuesta(objetivo, promedio, texto, contador)
