#!/bin/bash

# Este script es un programa interactivo que no recibe argumentos.
# Debe preguntarle al usuario que etiqueta desea buscar y mostrar por
# pantalla todas las imágenes que tengan esa etiqueta, junto con su descripción.

clear

# Verificacion de existencia de bases de datos
if [ ! -e imagenes.json ]
then
  echo "Error: falta archivo imagenes.json. Las imágenes no fueron descriptas aún."
  exit 1
fi

if [ ! -e etiquetas.json ]
then
  echo "Error: falta archivo etiquetas.json. Las imágenes no fueron etiquetadas aún."
  exit 2
fi

# Inicio de script
read -p "Ingrese la etiqueta a buscar (o presiona 'enter' para cancelar): " etiqueta 

if [ "$etiqueta" = "" ]
then
  echo "Saliendo..."
  sleep 1
fi

lista_imagenes=$(jq -r --arg etiq "$etiqueta" '.[$etiq][]' etiquetas.json 2> /dev/null) 

if [ $? -ne 0 ]
then
  echo "Error: no existe la etiqueta" # jq no encuentra la etiqueta
  exit 4
fi
  
for imagen in $lista_imagenes
do
  descripcion=$(cat imagenes.json | jq -r --arg img "$imagen" '.[$img]')

  jp2a --colors --invert $imagen
  echo "Descripción: '$descripcion'"
done

