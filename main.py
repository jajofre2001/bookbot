#Importaciones
from stats import contar_palabras, get_book_text, contar_letras, crear_lista
import sys



#Ejecucion
def main():
    #Funcion donde se va a ejecutar el codigo

    #Comprobamos si el usuario utiliza el programa de manera correcta y le indicamos su uso en el caso de que no sepa y cerramos el programa
    try:
        ruta_archivo = sys.argv[1] 

    except IndexError:

        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    
    else:

        text = get_book_text(ruta_archivo) 
        num_palabras = contar_palabras(text)
        letras = contar_letras(text)
        lista_texto = crear_lista(letras,num_palabras,ruta_archivo)
    


main()