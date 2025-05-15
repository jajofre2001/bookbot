#Este archivo contiene las funciones que seran usadas para analizar texto
#Importaciones
from re import sub
from string import ascii_lowercase
#Funciones
def get_book_text(file_path):
    #Funcion que extrae el texto de un archivo .txt
    #Ent: El path relativo hacia el archivo deseado (.txt)
    #Salida: Un string con el textp del archivo
    

    #Abre y lee el archivo de texto en un bloque with
    with open(file_path,"r") as f:
        text = f.read()

    #Regresa el texto en forma de string
    return text


def contar_palabras(texto):
    #Funcion que recibe un texto y cuenta cuantas palabras tiene 
    #Ent: Un string
    #Salida: Un int 
    
    num_palabras = 0
    #Preparamos el texto eliminando los \n, * y espacios en blanco dobles
    palabras = "".join(texto.split("\n"))
    palabras = "".join(palabras.split("*"))
    palabras = sub(r'\s+', ' ', texto)
    palabras_lista = palabras.split(" ")
    for palabra in palabras_lista:

        num_palabras += 1

    return num_palabras

def contar_letras(texto):
    #Funcion que cuenta las veces que aparece una letra
    #Entrada: Texto en forma de str
    #Salida: Un diccionario con las veces que se repite las letras
    diccionario_letras = {}

    #Lista de las letras
    abcederario = ascii_lowercase 

    #Preparamos el texto eliminando los \n, * y espacios en blanco dobles
    palabras = "".join(texto.split("\n"))
    palabras = "".join(palabras.split("*"))
    palabras = sub(r'\s+', ' ', texto)
    palabras_lista = palabras.split(" ") 
    
    #Creamos el diccionario 
    for i in abcederario:
        diccionario_letras[i] = 0

    for palabra in palabras_lista:
        for letra in palabra.lower():

            if letra in abcederario:
                diccionario_letras[letra] += 1

            else:
                continue

    return diccionario_letras


def crear_lista(diccionario_letras, cantidad_palabras, ruta_archivo):
    #Funcion que recibe el diccionario de letras y lo entrega un str ordenado en cantidad
    #Entrada: Diccionario
    #Salida: str
    #Escribimos el encabezado

    encabezado = f"""============ BOOKBOT ============
Analyzing book found at {ruta_archivo}...
----------- Word Count ----------
Found {cantidad_palabras} total words
--------- Character Count -------\n"""
    pie = "============= END ==============="

    #Ordenamos el diccionario de mayor a menor
    diccionario_ordenada = dict(sorted(diccionario_letras.items(),key = lambda item: item[1], reverse=True))
    texto_int = ""
    for keys in diccionario_ordenada:
        texto_int = texto_int + f"{keys}: {diccionario_ordenada[keys]}\n" 
    
    texto_completo = encabezado + texto_int + pie
    print(texto_completo)

    
            


