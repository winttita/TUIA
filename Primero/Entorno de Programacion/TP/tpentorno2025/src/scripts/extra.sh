#!/bin/bash


#Función para contar imágenes por etiqueta
contar_por_etiqueta() {
	read -p "Ingrese una etiqueta para contar la cantidad de imágenes: " etiqueta
	
  if jq -e --arg etq "$etiqueta" 'has($etq)' etiquetas.json &> /dev/null
  then
    # verifica si existe la etiqueta en el archivo js si existe cuenta la cantidad de imagenes
    cantidad=$(cat etiquetas.json | jq -r --arg etq "$etiqueta" '.[$etq][]' | wc -l)
    echo "La etiqueta $etiqueta tiene $cantidad imágen(es)."
	else
  	echo "$etiqueta no existe"
	fi
}



clear
$SOURCEDIR/menu/checks.sh
COLUMNS=1
PS3="Elija una opción: "
select OPCION in "Limpiar carpeta de imágenes."  \
                 "Contar imágenes por etiqueta." \
                 "Mostrar etiquetas disponibles." \
		             "Volver al menú inicial." 
do
  case $REPLY in
    1) (cd $IMAGESDIR && (rm * 2> /dev/null && echo "Se ha limpiado la carpeta imagenes") || echo "No existen archivos en la carpeta imagenes") ;;
  	2) (cd $IMAGESDIR && contar_por_etiqueta) ;;
  	3) (cd $IMAGESDIR && clear && (jq 'keys' etiquetas.json 2> /dev/null || echo "No existe el archivo 'etiquetas.json'") ) ;; 
  	4) exit 0 ;;
    *) echo "Opción incorrecta."
  esac

  read -p "Presione enter para continuar..."
  clear
  $SOURCEDIR/menu/checks.sh
  COLUMNS=1
done
