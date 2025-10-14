#!/bin/bash

if [[ $# < 1 ]]; then
	echo "Debe ingresar al menos un nombre de directorio a crear."
	exit 1
fi

for DIRECTORIO in $@
do
	mkdir $DIRECTORIO 2> /dev/null
	if [[ $? != 0 ]]; then
		echo "No se pudo crear la carpeta $DIRECTORIO"
		continue
	fi
	echo "Se creo correctamente la carpeta $DIRECTORIO"
done
