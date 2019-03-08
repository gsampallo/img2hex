import os
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt


def main(argv):

    imagen = argv[0]

    maximoCaracteres = int(argv[2]) #especifica cuandos caracteres se utilizaran 
    maximoFilas = int(argv[3])

    maximoColumnasPixel = maximoCaracteres*5
    maximoFilasPixel = maximoFilas*8

    archivo = argv[1]
    if os.path.exists(archivo):
        os.remove(archivo)

    img = cv2.imread(imagen,0)
    #print "Dimensiones original: ",img.shape
    ret,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY)

    if((img.shape[0] > 8) or (img.shape[1] > 5)):
        print ("Se redimensiona la imagen")
        img = cv2.resize(img,(int(maximoColumnasPixel),int(maximoFilasPixel)))

    cv2.imwrite( "imagen1.jpg", img )


    valores = (16,8,4,2,1)

    caracter = 0

    c = 0
    f = 0
    while c < maximoCaracteres:

        resultado = [0,0,0,0,0,0,0,0]
        f = 0
        while f < maximoFilas:

            #Se define los intervalos de cada cuadrante dentro de la imagen
            inicialX = 0
            finalX = 5
            if(c > 0):
                inicialX = c*5+1
                finalX = c*5+5

            inicialY = 0
            finalY = 8
            if(f > 0):
                inicialY = f*8+1
                finalY = f*8+8

            f1 = 0
            for fila in range(inicialY,finalY):
                c1 = 0
                for col in range(inicialX,finalX):
                
                    if(img[fila][col] == 0):
                        #print (f1,c1)
                        resultado[f1] = resultado[f1] + valores[c1]   
                    c1 = c1 + 1
                f1 = f1 + 1 

            file = open(archivo,"a")
            file.write("c")
            file.write(str(caracter))
            file.write(" = bytearray([")
            a = False
            for fila in range(0,8):
                if(a):
                    file.write(",")
                file.write(hex(resultado[(fila)]))
                a = True
            file.write("])\n")
            file.write("lcd.custom_char(")
            file.write(str(caracter))
            file.write(",")
            file.write("c")
            file.write(str(caracter))
            file.write(")\n")

            file.close()
            caracter = caracter + 1
            f = f + 1

        c = c + 1
    print "Se genero el archivo ",archivo

if __name__ == "__main__":
    if(len(sys.argv[1:]) == 0):
        print ("La forma de uso es de la siguiente manera:")
        print (" python img2hex.py img output columnas filas")
        print ("img: es la imagen que deseamos convertir en hexadecimal, se aceptan jpg, png")
        print ("output: es el archivo python que tendra el resultado del proceso, desde ahi se podra copiar y pegar al propio programa")
        print ("columnas: la cantidad de caracteres que deseamos utilizar en el display, para el caso del display de 16x2, el maximo sera 16")
        print ("filas: la cantidad de filas que utilizaremos del display.")
        print ("")
        print ("Lo recomendable es utilizar una sola fila, visualmente tiene mejor resultado")
        print( "")
        print( " github.com/gsampallo\n")
    else:   

        main(sys.argv[1:])
        #main(sys.argv)