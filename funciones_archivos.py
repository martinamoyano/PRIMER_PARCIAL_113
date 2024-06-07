import re
import json

def parser_csv(path: str)-> list:
    """
    Lee un archivo CSV y devuelve una lista de diccionarios basada en su contenido.

    Args:
    - path (str): Ruta del archivo CSV.

    Returns:
    - list: Lista de diccionarios con la información leída del archivo CSV.
    """
    lista = []
    try :
        with open (path, "r", encoding= "utf8") as archivo:
            campo = re.split (",|\n", archivo.readline())
            for lineas in archivo:
                registro = re.split (",|\n", lineas)
                diccionario = {}
                diccionario = {
                campo[0]: int (registro [0]),
                campo[1]: registro [1],
                campo[2]: registro [2],
                campo[3]: int (registro [3]),
                }

                lista.append (diccionario)
        return lista
    except FileNotFoundError:
        print (f"Error. La ruta '{path}' no existe")

#--------------------------------------------------------------

def generar_csv(path: str, lista: list):
    """
    Guarda una lista de diccionarios en un archivo CSV.

    Args:
    - path (str): Ruta del archivo CSV.
    - lista (list): Lista de diccionarios a guardar en el archivo CSV. Cada diccionario debe contener las claves 
      'id_bike', 'nombre', 'tipo', y 'tiempo'.

    Returns:
    - None
    """
    with open(path, "w", encoding="utf-8") as archivo:
        for elemento in lista:
            linea = f"{elemento['id_bike']},{elemento['nombre']},{elemento['tipo']},{elemento['tiempo']}\n"
            archivo.write(linea)



#------------------------------


def parser_json(path:str)-> list:
    """
    Lee un archivo JSON y devuelve una lista de diccionarios basada en su contenido.

    Args:
    - path (str): Ruta del archivo JSON.

    Returns:
    - list: Lista de diccionarios con la información leída del archivo JSON.
    """
    with open (path, "r") as archivo:
        diccionario = json.load(archivo)
    
    return diccionario["key"]




def generar_json(path: str, lista:list):
    """
    Guarda una lista de diccionarios en un archivo JSON.

    Args:
    - path (str): Ruta del archivo JSON.
    - lista (list): Lista de diccionarios a guardar en el archivo JSON.

    Returns:
    - None
    """
    with open (path, "w") as archivo:
        json.dump(lista, archivo, indent = 4)

