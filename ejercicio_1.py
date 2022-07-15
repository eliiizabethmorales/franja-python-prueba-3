import numpy as np
import random
def escribirtxt():
    nombre_fichero = "./numeros_prueba.txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for l in range(20):
            numerosaleatorios = random.randint(100, 1000)
            numeros_en_fichero = str(numerosaleatorios)
            file.write(numeros_en_fichero)
            file.write("\n")
def leer():
    numerofichero = []
    with open("./numeros_prueba.txt","r") as file:
        for numeros_en_fichero in file:
            numerofichero.append(int(numeros_en_fichero))
    numeros_impares = []
    for x in numerofichero:
        if x %2 !=0:
            numeros_impares.append(x)
    return numeros_impares

def main ():
    escribirtxt()

    numeros_impares = leer()

    print(numeros_impares)

    arreglo_numpy = np.array(numeros_impares)
    print(arreglo_numpy.ndim)

if __name__== '__main__':
    main()