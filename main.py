#Importaciones
import re
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
    palabras = re.sub(r'\s+', ' ', texto)
    palabras_lista = palabras.split(" ")
    for palabra in palabras_lista:

        num_palabras += 1

    return num_palabras

#Ejecucion
def main():
    text = get_book_text("./books/frankenstein.txt") 
    num_palabras = contar_palabras(text)
    print(f"{int(num_palabras)} words found in the document")


main()