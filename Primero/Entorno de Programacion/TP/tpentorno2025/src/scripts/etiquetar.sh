#!/bin/bash

# Este script trabaja sobre archivos de la carpeta actual que terminan en .jpg,
# clasificándolos usando YOLO y agregando una descripción de la imagen usando Moondream:
#
# Deben crear dos archivos JSON, etiquetas.json e imagenes.json (ver la estructura propuesta
# en ../../docs/aclaraciones.md).
# Usar el comando `jq` para manipular los archivos JSON.
# Asegúrese de devolver un valor de salida acorde a la situación.

clear
ls *.jpg &> /dev/null

if [ $? -ne 0 ]; then
  echo "No existe ninguna imagen"
  exit 1  # No hay imágenes en el archivo actual
fi

# Inicializa archivos JSON
if [ ! -f "etiquetas.json" ]; then
  echo "{}" > etiquetas.json
fi

if [ ! -f "imagenes.json" ]; then
  echo "{}" > imagenes.json
fi

# Recorro el directorio con imagenes, las clasifico y describo.
for imagen in *.jpg; do
  echo "Procesando: $imagen"
       
  # Creacion de descripcion con Ollama
	resultado_imagen=$(grep $imagen imagenes.json)

	if [ "$resultado_imagen" = "" ]; then
  	echo "Describiendo imagen..."

    descripcion=$(ollama run moondream "{'content': 'Describe me this image', 'images': './$imagen'}")
    resultado=$(jq --arg desc "$descripcion" --arg img "$imagen" '.[$img] += [$desc]' imagenes.json) # Se agrega la descripcion nueva con la imagen correspondiente

    echo $resultado > imagenes.json # Se guardan los resultados nuevos en el archivo .json
    echo "Se ha agregado la descripción de $imagen"

  else
    echo "La imagen $imagen ya tiene descripción. Verificando etiquetas..."

	fi

  # Creacion de etiquetas con yolo
	etiquetas=$(yolo predict source="$imagen" | grep "$imagen" | cut -d " " -f 5- | grep -oE "[[:alpha:]]+[[:space:]]?[[:alpha:]]+" | grep -v '^ms$' | tr ' ' '_') # Se crea una lista de etiquetas según los resultados de yolo
	
  for etiqueta in $etiquetas; do
    resultado_etiqueta=$(jq --arg etiq "$etiqueta" '.[$etiq]' etiquetas.json | grep $imagen)

    if [ "$resultado_etiqueta" = "" ]; then # Si la imagen ya está agregada a la etiqueta que le corresponde, omite el paso
  	  echo "Agregando $imagen a etiqueta $etiqueta..."

    	resultado=$(jq --arg etiq "$etiqueta" --arg img "$imagen" '.[$etiq] += [$img]' etiquetas.json)

    	echo $resultado > etiquetas.json
    	echo "Imagen agregada."

    else
      echo "La imagen $imagen ya se encuentra en la etiqueta $etiqueta"

  	fi
	done

	echo "" #Salto de linea despues de procesar una imagen
done

