def capturar_datos():
    id = input("digite su codigo de identificacion: ")
    return id
    
def analizar_datos(id ,cont_permitidos, mensajes, cont_no_permitidos):
    codigo_especial='tete'
    
    if id == codigo_especial:
        cont_permitidos +=1
        mensajes += 'acceso permitido\n'
    else:
        cont_no_permitidos +=1
        mensajes += 'acceso denegado\n'
        
    return cont_permitidos, cont_no_permitidos, mensajes

def mostrar_resultados(cont_permitidos, cont_no_permitidos, mensajes):
    print("mensaje de acceso: ")
    print(mensajes)
    print("total de accesos permitidos:", cont_permitidos)
    print("total de accesos no permitidos", cont_no_permitidos)

cont_permitidos = 0
cont_no_permitidos = 0
mensajes = ""

while True:
    id = capturar_datos()
    
    if id == 'SALIR':
        break

    cont_permitidos, cont_no_permitidos, mensajes = analizar_datos(
        id,
        cont_permitidos,
        mensajes,
        cont_no_permitidos
    )

mostrar_resultados(cont_permitidos, cont_no_permitidos, mensajes)
