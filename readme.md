# img2hex

img2hex es un script en python que permite convertir una imagen a formate hexadecimal para que pueda ser vista en un LCD desde MicroPython o Arduino.

![alt text](https://raw.githubusercontent.com/gsampallo/img2hex/master/intro.jpg "Diagrama")

## Instalacion

Es necesario instalar OpenCV para poder procesar las imagenes.
En mi caso lo instale desde la consola de la siguiente manera:

install opencv-python
install opencv-contrib-python
install matplotlib

## Forma de uso

La forma de utilizar la herramienta es la siguiente:
    python img2hex.py img output column row

- img:  indica la imagen que deseamos convertir a formato hexadecimal, se aceptan diferentes formatos (jpg, png).
- output:  es el archivo resultado del proceso, contiene el codigo python con los caracteres resultantes del proceso.
- column:  cantidad de caracteres horizontales que deseamos que ocupe la imagen. Para el caso de los display de 16x2, el maximo es 16.
- row:  cantidad de filas que utilizara la imagen.

Lo recomendable es que se utilice una sola fila, visualmente queda mejor. Si bien el script conviente las imagenes a blanco y negro, y las redimensiona para que se correspondan con el tamaño de la reticula elegida, es aconsejable utilizar imagenes en blanco y negro, y de muy baja resolucion para tener mejores resultados.

## Ejemplo

Dentro de la carpeta example hay varias imagenes que se utilizaron para construir la demo del pacman.
![alt text](https://raw.githubusercontent.com/gsampallo/img2hex/master/dmeo.jpg "Demo")