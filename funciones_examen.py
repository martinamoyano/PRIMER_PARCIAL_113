from funciones_archivos import *
from funciones_genericas import *
from random import randint
from validaciones import *

# Cargar archivo .CSV
def cargar_archivo()-> list:
    """
    Carga los datos de un archivo CSV y los convierte en una lista de diccionarios.

    Args:
    - None

    Returns:
    - Retorna la lista cargada con los datos del CSV.
    """
    path = input("Por favor ingrese la ruta del archivo .CSV a cargar: ")
    lista_datos = parser_csv(path)
    if lista_datos != None:
        print("¡Archivo cargado con éxito!")
    return lista_datos

# Imprimir lista
def imprimir_lista(lista: list):
    """
    Valida y muestra una lista.

    Args:
    - lista (list): Lista de diccionarios.

    Returns:
    - None
    """
    if validar_lista (lista) == True:
        mostrar_lista(lista)

# Asignar tiempos
def asignar_tiempo_bicicleta(bicicleta)-> dict:
    """
    Asigna un tiempo aleatorio entre 50 y 120 a la bicicleta.

    Args:
    - bicicleta (dict): Diccionario que representa una bicicleta.

    Returns:
    - dict: El diccionario de la bicicleta con el tiempo asignado.
    """
    bicicleta['tiempo'] = randint(50, 120)
    return bicicleta

def asignar_tiempos(lista:list)-> bool:
    """
    Asigna tiempos a cada bicicleta en la lista utilizando una función de mapeo y muestra los resultados.

    Args:
    - lista (list): Lista de diccionarios que contienen información sobre bicicletas.

    Returns:
    - bool: `True` si los tiempos fueron asignados y cargados correctamente, `False` en caso contrario.

    Raises:
    - TypeError: Si se produce un error durante la asignación de tiempos.
    """
    try:
        lista_datos = map_list(asignar_tiempo_bicicleta, lista)
        mostrar_lista(lista_datos)
    except TypeError as e:
        print (e)
    if lista_datos:
        tiempos_cargados = True
    return tiempos_cargados

# Informar ganador
def definir_ganador(lista: list) -> dict:
    """
    Define el ganador de la carrera de bicicletas basándose en el menor tiempo.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el nombre del ganador y el tiempo si hay un único ganador,
            o una lista de nombres y el tiempo si hay un empate.
    """
    ganador = calcular_minimo_dict(lista, "tiempo")
    tiempo_ganador = ganador["tiempo"]
    
    bicicletas_empatadas = []
    for bicicleta in lista:
        if bicicleta["tiempo"] == tiempo_ganador:
            bicicletas_empatadas.append(bicicleta["nombre"])

    if len(bicicletas_empatadas) == 1:
        return {"Ganador": ganador["nombre"], "Tiempo": tiempo_ganador}
    return {"Empate": bicicletas_empatadas, "Tiempo": tiempo_ganador}

def informar_ganador(lista: list) -> dict:
    """
    Informa el resultado de la carrera, mostrando el ganador o los empatados en tiempo.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el resultado de la carrera, indicando el ganador o los empatados.
    """
    resultado_carrera = definir_ganador(lista)
    print("------------------------------")
    print("Resultado de la carrera")
    print("------------------------------")
    mostrar_diccionario(resultado_carrera)

# Filtrar por tipo
def filtrar_por_tipo(lista: list) -> list | None:
    """
    Filtra una lista de bicicletas por tipo ingresado por el usuario.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - list: Lista filtrada de diccionarios con el tipo de bicicleta solicitado.
    """
    tipos = list(set(mapear_campo(lista, "tipo")))
    tipo = input("Ingrese el tipo de bicicleta que desea filtrar [MTB, BMX, PLAYERA, PASEO]: ").upper()

    if buscar_en_lista(tipos, tipo):
        lista_filtrada = filtrar(lista, "tipo", tipo)
        return lista_filtrada
    else:
        return None
    
def filtrar_bicicletas(lista: list):
    """
    Filtra la lista de bicicletas por tipo y genera un archivo CSV con los resultados.

    Args:
    - lista (list): Lista de diccionarios que contienen información sobre bicicletas.

    Returns:
    - None: La función no retorna ningún valor, pero genera un archivo CSV si la lista filtrada es válida.

    Prints:
    - Mensajes indicando el éxito de la operación o si el tipo de bicicleta no es válido.
    """
    lista_filtrada = filtrar_por_tipo(lista)
    if validar_lista(lista_filtrada):
        primer_elemento = lista_filtrada[0]
        tipo = primer_elemento["tipo"]
        path = f"{tipo}.csv"
        generar_csv(path, lista_filtrada)
        print(f"¡Archivo creado con exito en {path}!")
    else:
        print("TIPO DE BICICLETA NO VÁLIDO.")

# Informar promedio por tipo
def informar_promedio_tipo(lista: list) -> dict:
    """
    Calcula y muestra el promedio de tiempo por cada tipo de bicicleta en la lista.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - dict: Diccionario con el tipo de bicicleta como clave y su promedio de tiempo como valor.
    """
    tipos = set(mapear_campo(lista, "tipo"))
    promedios = {}

    for tipo in tipos:
        bicicletas_tipo = filtrar(lista, "tipo", tipo)
        tiempos = mapear_campo(bicicletas_tipo, "tiempo")
        if tiempos:
            promedio = calcular_promedio(tiempos)
        else:
            promedio = 0
        promedios[tipo] = promedio

    return promedios

# Mostrar las posiciones
def mostrar_posiciones(lista:list)-> bool:
    """
    Ordena la lista de bicicletas por tipo y tiempo, y muestra las posiciones.

    Args:
    - lista (list): Lista de diccionarios que contienen información sobre bicicletas.

    Returns:
    - bool: True si las posiciones se muestran correctamente.

    Prints:
    - Detalles de cada bicicleta ordenada por tipo y tiempo.
    """
    ordenar_lista_doble_criterio(lista, "tipo", "tiempo")
    posiciones = True
    for bicicleta in lista:
        print(f'Tipo: {bicicleta["tipo"]}, Tiempo: {bicicleta["tiempo"]}')
    return posiciones

# Guardar posiciones
def guardar_posiciones(lista: list):
    """
    Guarda las posiciones de las bicicletas en un archivo JSON llamado 'posiciones.json'.

    Args:
    - lista (list): Lista de diccionarios que contiene información de bicicletas.

    Returns:
    - None
    """
    generar_json("posiciones.json", lista)
    print("Posiciones guardadas en 'posiciones.json'.")
