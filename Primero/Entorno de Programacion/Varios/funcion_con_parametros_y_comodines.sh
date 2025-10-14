#!/bin/bash

buscar_archivos(){
	
	local extension=$1
		
	read -p "Ingrese la ruta del directorio donde desea buscar archivos de texto y scripts: " archivo

	find "$archivo" -name "*.$1"
}

read -p "Ingrese una extension (ej: .txt): " extension

buscar_archivos "$extension"
