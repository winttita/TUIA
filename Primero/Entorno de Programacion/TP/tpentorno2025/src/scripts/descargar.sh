#!/bin/bash

# Este script debe descargar una sola imagen desde internet en la carpeta actual.
# Puede recibir un argumento opcional indicando la clase de la imagen.
# El nombre del archivo deberá ser único, una opción para evitar repetición de imágenes
# y asegurar que sea único se puede usar su suma de verificación.
# Las imágenes descargadas tienen extensión .jpg.
# Asegúrese de devolver un valor de salida acorde a la situación.

#clear

if [ $# -eq 1 ]
then
	clase="$1"
	url="https://tuia-edp.org/random-image?category=$clase"
else
	url="https://tuia-edp.org/random-image"
fi

if wget -O "imagen" $url # Descarga la imagen con el nombre temporal "imagen"
then
	suma=$(sha256sum imagen | cut -d " " -f1)
	nombre_final="$suma.jpg"

	mv ./imagen "$nombre_final" # Renombra a su hash resultante
	echo "Descarga exitosa!"
else
	rm imagen
	echo "Error: No se pudo descargar la imagen. Categoría no admitida"
	exit 1
fi


