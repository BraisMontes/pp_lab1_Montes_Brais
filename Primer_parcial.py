import json
import re

def parse_json(nombre_archivo:str)->list:
    """
    La funcion se encarga de abrir el archivo Json
    Parametros: nombre_archivo de tipo str para pasarle el nombre del archivo
    Retorna la lista de tipo Json
    """
    lista=[]
    with open(nombre_archivo,"r",encoding="UTF-8") as archivo :
        dict = json.load(archivo)
        lista = dict["jugadores"]
    return lista

lista_jugadores = parse_json("Parcial Utn\dt.json")


def imprimir_jugadores(lista:list):
    """
    La funcion se encarga de imprimir los jugadores
    Parametros: Lista de jugadores de tipo Json
    No retorna nada
    """
    if len(lista) == 0:
        return 0
    else:
        for i in range(len(lista)):
            nombre = lista[i]["nombre"]
            print(f"El indice es : {i} y el nombre es : {nombre}\n")
#1)Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
#Nombre Jugador - Posición. Ejemplo:
#Michael Jordan - Escolta
def imprimir_nombre_y_posicion_jugadores(lista:list):
    """
    La funcion se encarga de imprimir los nombres de los jugadores y sus respectivas posiciones
    Parametros: Lista de jugadores de tipo Json
    retorna el mensaje a dar 
    """
    
    if len(lista) > 0:
        for jugador in lista:
            texto = "Nombre jugador: {0} - Posicion: {1}\n".format(jugador["nombre"],jugador["posicion"])
            print(texto,end="")
    else:
        print("error")
    return texto
#2)Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
def imprimir_jugador_segun_indice(lista:list,indice:int):
    """
    La funcion se encarga de imprimir los jugadores segun el indice pasado por parametro
    Parametros: Lista de jugadores de tipo Json y el indice de la posicion que desea imprimir
    No retorna nada
    """
    if len(lista) == 0:
        return 0
    else:
        imprimir_jugadores(lista)
        indice_elegido = lista[indice]["nombre"]
        print(f"El nombre del indice elegido es {indice_elegido}\n")   
        for key,value in lista[indice]["estadisticas"].items():
            print(f"{key} = {value}")
    
#3)Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples."estadisticas_jugadores.csv"
def guardar_mensaje_archivo_csv(lista:list):
    """
    La funcion se encarga de elaborar un mensaje para guardar como archivo Csv
    Parametros: Lista de jugadores de tipo Json
    Retorna el mensaje con el contenido para escribir en un Csv
    """
    if len(lista) == 0:
        return 0
    else:
        estadisticas = [] 
        claves = []
        valores = []
        imprimir_jugadores(lista)         
        indice = input("Ingrese el índice del 0 al 11 para mostrar la información del jugador: ")
        if re.match(r'[0-9]|1[0-1]', indice):
            indice = int(indice)
            if indice <= len(lista):
                estadisticas.append(lista[indice]["estadisticas"])
        for estadistica in estadisticas:
            for key,value in estadistica.items():
                claves.append(key) 
                valores.append(str(value))
            
    claves_separadas = ",".join(claves)
    valores_separados = ",".join(valores)
    mensaje = f"{claves_separadas}\n{valores_separados}"
    return mensaje

def generar_csv(dato:str):  
    """
    La funcion se encarga de generar un archivo Csv
    Parametros: dato de tipo str, con el mensaje para escribir el archivo Csv
    No retorna nada
    """
    with open("Estadisticas.csv","w") as archivo: 
        aux_archivo = archivo.write(dato)
        if aux_archivo == True:
            print("Se creo el archivo correctamente")
        else:
            print("Error al crear el archivo")
            

#4)Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.
def buscar_nombre_y_mostrar_logros(lista:list, nombre_jugador:str)->dict:
    """
    La funcion se encarga de buscar un nombre del jugador y mostrar sus logros
    Parametros: Lista de jugadores de tipo Json y el nombre del jugador de tipo str para poder acceder a sus logros
    Retorna un jugador de tipo dict con sus logros
    """
    if len(lista) == 0:
        return 0
    else:
        for jugador in lista:
            if re.search(nombre_jugador,jugador["nombre"],re.IGNORECASE):
                return jugador
        

#5)Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente. 
def calcula_promedio(lista:list,campo_uno:str,campo_dos:str)->float:
    """
    La funcion se encarga de calcular un promedio dependiendo los parametros que le pasen
    Parametros: Lista de jugadores de tipo Json y los campos de tipo str para acceder a los campos de el diccionario
    Retorna el resultado del promedio 
    """
    
    acumulador=0
    contador=0
    resultado = 0
    if len(lista)== 0:
        return 0 
    
    for jugador in lista:
        acumulador = acumulador + jugador[campo_uno][campo_dos]
        contador += 1
    
    if(contador > 0 ):
        resultado = acumulador / contador
    return resultado  

def ivan_sort_B(lista:list,campo:str,flag_orden:bool):
    """
    La funcion se encarga ordenar la lista alfabeticamente de manera ascendete o descendente
    Parametros: Lista de jugadores de tipo Json y una variable de tipo booleano para determinar si quiere ordenar de manera ascendente o descendente
    Retorna la lista ordenada
    """
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista[indice_A][campo] < lista[indice_A+1][campo] \
             or flag_orden == True and lista[indice_A][campo] > lista[indice_A+1][campo]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True
    return lista

             
#6)Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.
def verifico_jugador_miembro_del_salon(lista:list,nombre_jugador:str):
    """
    La funcion se encarga de buscar un nombre del jugador y determinar si es Miembro del Salon de la Fama del Baloncesto.
    Parametros: Lista de jugadores de tipo Json y el nombre del jugador de tipo str para poder acceder a sus logros
    No retorna nada
    """
    
    if len(lista) == 0:
        return 0
    else:
        for jugador in lista:
            if jugador["nombre"] == nombre_jugador:
                if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                    print(f"{jugador['nombre']} es miembro del Salón de la Fama del Baloncesto")
                else:
                    print(f"{jugador['nombre']} no es miembro del Salón de la Fama del Baloncesto")

#7)Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
#8)Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
#9)Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
#13)Calcular y mostrar el jugador con la mayor cantidad de robos totales.
#14)Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.

def calcular_y_mostrar_mayor (lista:list,campo_uno:str,campo_dos:str):
    """
    La funcion se encarga de calcular y buscar el mayor en una determinada estadistica pasada por parametro
    Parametros: Lista de jugadores de tipo Json y los campos de tipo str para acceder a los campos del diccionario
    Retorna El jugador con el maximo de estadistica pasada por parametro
    """
    aux_maximo = 0
    jugador_maximo= None
    for jugador in lista:
        cantidad_total = jugador[campo_uno][campo_dos]
        if cantidad_total > aux_maximo:
            aux_maximo = cantidad_total
            jugador_maximo = jugador["nombre"]
    return jugador_maximo


#10) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.
#11)Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.
#12)Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.
#15)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
#18)Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.

def mostrar_jugador_mas_puntos_que_promedio(lista:list,campo_uno:str,campo_dos:str):
    """
    La funcion se encarga de pedir un valor al usuario y determinar que jugadores tienen mas promedio en determinada estadistica pasada por parametro que ese valor.
    Parametros: Lista de jugadores de tipo Json y los campos de tipo str para poder acceder a sus campos del diccionario
    No retorna nada
    """
    valor_usuario = input("Ingrese el valor que desea comparar con el promedio.")
    valor_usuario = float(valor_usuario)
    #if re.search(r'^[-+]?\d*\.?\d+$',valor_usuario): Me tira error al validar
    print(f"Jugadores que superan el valor de {campo_dos}:")
    for jugador in lista:
            if valor_usuario < jugador[campo_uno][campo_dos]:
                print(f'Jugador: {jugador["nombre"]} - Promedio: {jugador[campo_uno][campo_dos]}')
            else: print("Error con el valor ingresado ")
    
#16)Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
def calcular_mostrar_promedio_menos_el_peor_jugador(lista:list,campo_uno:str,campo_dos:str):
    """
    La funcion se encarga de calcular el promedio de puntos por partido excepto jugador con menos puntos por partido.
    Parametros: Lista de jugadores de tipo Json y las variables campos de tipo str para poder acceder a sus campos
    Retorna el promedio de puntos por partido sin el jugador con menos puntos.
    """
    aux_minimo = 10000
    acumulador = 0
    contador = 0
    jugador_con_menos_puntos = None
    for jugador in lista:
        cantidad_de_puntos = jugador[campo_uno][campo_dos]
        if cantidad_de_puntos < aux_minimo:
             aux_minimo = cantidad_de_puntos
             jugador_con_menos_puntos = jugador["nombre"]
    for jugador in lista:
        acumulador = acumulador + jugador[campo_uno][campo_dos]
        contador += 1
    
    if(contador > 0 ):
        resultado_sin_minimo = acumulador / contador
        resultado_total = resultado_sin_minimo - aux_minimo
    print("El jugador con menos puntos es : {0} con {1} puntos".format(jugador_con_menos_puntos,aux_minimo))    
    return resultado_total 

#17)Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos

def jugador_con_mas_cantidad_logros (lista:list):
    """
    La funcion se encarga de buscar al jugador con mas cantidad de logros 
    Parametros: Lista de jugadores de tipo Json 
    Retorna al jugador con mas logros
    """
    aux_len = 0
    jugador_con_mas_logros = None
    for jugador in lista:
        cantidad_logros = len(jugador["logros"])
        
        if aux_len < cantidad_logros:
            aux_len = cantidad_logros
            jugador_con_mas_logros = jugador["nombre"]
    print("Cantidad de logros {0}".format(aux_len))        
    return jugador_con_mas_logros

#19Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas

def jugadores_mayor_temporadas(lista:list,campo_uno:str,campo_dos:str)->list:
    """
    La funcion se encarga de calcular al jugador con mas temporadas
    Parametros: Lista de jugadores de tipo Json y las variables campo_uno y campo_dos de tipo str para poder acceder a sus estadisticas
    Retorna una lista con los jugadores con mas temporadas del dream team
    """
    
    max_temporadas = max(jugador[campo_uno][campo_dos] for jugador in lista)
    print(max_temporadas)
    jugadores_max_temporadas = []
    for jugador in lista:
        
        if jugador[campo_uno][campo_dos] == max_temporadas:
            jugadores_max_temporadas.append(jugador['nombre'])
    
    return jugadores_max_temporadas
#20)Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
def ingresar_valor_mostrar_jugadores_ordenados_por_posicion_cancha(lista:list):
    pass
    
    
while True : 
    respuesta = input("\n 1-Mostrar la lista de todos los jugadores del Dream Team\n 2-Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas   \n 3-Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario guardar las estadísticas de ese jugador en un archivo CSV \n 4-Permitir al usuario buscar un jugador por su nombre y mostrar sus logros \n 5- calcular y mostrar el promedio de puntos por partido de todo el Dream Team, ordenado por nombre de manera ascendente \n 6-Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del salon de la fama del baloncesto \n 7- salir\n 8- \n 9- \n 10- \n 11- \n 12- \n 13- \n 14- \n 15- \n 16- \n 17- \n 18- \n 19- \n 20- \n 21 -salir")
    match (int(respuesta)): 
        case 1: 
            lista_jugadores = parse_json("Parcial Utn\dt.json")
            resultado = imprimir_nombre_y_posicion_jugadores(lista_jugadores)
            print(resultado)
        case 2:
            imprimir_jugador_segun_indice(lista_jugadores,0)
        case 3:
            mensaje =  guardar_mensaje_archivo_csv(lista_jugadores)
            generar_csv(mensaje)
            
        case 4:
            nombre_jugador = input("Ingrese el nombre del jugador que desea ver los logros")
            nombre_jugador = str(nombre_jugador)
            jugador = buscar_nombre_y_mostrar_logros(lista_jugadores,nombre_jugador)
            for key,value in jugador.items():
                print(f"{key} - {value}")
        case 5:
            resultado_promedio = calcula_promedio(lista_jugadores,"estadisticas","promedio_puntos_por_partido")
            print(f"El resultado del promedio de puntos por partido es de: {resultado_promedio}")
            resultado_ordenamiento = ivan_sort_B(lista_jugadores,"nombre",True)
            print("Jugadores ordenados alfabeticamente de manera ascendente : ")
            for i in range(len(resultado_ordenamiento)):
                print(f"Jugaodr : {resultado_ordenamiento[i]['nombre']} y su promedio : {resultado_ordenamiento[i]['estadisticas']['promedio_puntos_por_partido' ]}")
            
            
        case 6:
            verifico_jugador_miembro_del_salon(lista_jugadores,"Christian Laettner")
        case 7:
            jugador_con_mas_rebotes = calcular_y_mostrar_mayor(lista_jugadores,"estadisticas","rebotes_totales")
            print(f"El jugador con mas rebotes del dream team es : {jugador_con_mas_rebotes}")
        case 8:
            jugador_mayor_porcentaje_tiros = calcular_y_mostrar_mayor(lista_jugadores,"estadisticas","porcentaje_tiros_de_campo")
            print(f"El jugador con mas porcentaje de tiro del dream team es : {jugador_mayor_porcentaje_tiros}")
        case 9:
            jugador_mayor_asistencias = calcular_y_mostrar_mayor(lista_jugadores,"estadisticas","asistencias_totales")
            print(f"El jugador con mas asistencias del dream team es : {jugador_mayor_asistencias}")
        case 10:
            
            mostrar_jugador_mas_puntos_que_promedio(lista_jugadores,"estadisticas","promedio_puntos_por_partido")
        case 11:
            mostrar_jugador_mas_puntos_que_promedio(lista_jugadores,"estadisticas","promedio_rebotes_por_partido")
        case 12:
            mostrar_jugador_mas_puntos_que_promedio(lista_jugadores,"estadisticas","promedio_asistencias_por_partido")
        case 13:
             jugador_con_mas_robos = calcular_y_mostrar_mayor(lista_jugadores,"estadisticas","robos_totales")
             print(f"El jugador con mas robos del dream team es: {jugador_con_mas_robos}")
        case 14:
            jugador_con_mas_bloqueos = calcular_y_mostrar_mayor(lista_jugadores,"estadisticas","bloqueos_totales")
            print(f"El jugador con mas bloqueos del dream team es: {jugador_con_mas_bloqueos}")
        case 15:
            mostrar_jugador_mas_puntos_que_promedio(lista_jugadores,"estadisticas","porcentaje_tiros_libres")
        case 16:
            promedio_sin_jugador_con_menos_puntos = calcular_mostrar_promedio_menos_el_peor_jugador(lista_jugadores,"estadisticas","promedio_puntos_por_partido")
            print("El promedio de los jugadores sin la menor puntuacion es de : {0}".format(promedio_sin_jugador_con_menos_puntos))
        case 17:
            jugador_mas_logros = jugador_con_mas_cantidad_logros (lista_jugadores)
            print("El jugador con mas logros del dream team es {0}".format(jugador_mas_logros))       
        case 18:
            mostrar_jugador_mas_puntos_que_promedio(lista_jugadores,"estadisticas","porcentaje_tiros_triples")
        case 19:
            jugadores_con_mas_temporadas = jugadores_mayor_temporadas(lista_jugadores,"estadisticas","temporadas")
            print(f"Los jugadores con mas temporadas son: {jugadores_con_mas_temporadas}")
        case 20:
            print("No pude terminarla, me exploto la cabeza")
        case 21:
            break