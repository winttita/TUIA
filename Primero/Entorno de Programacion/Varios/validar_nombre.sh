#!/bin/bash

read -p "Ingrese un nombre: " nombre

while [[ ! "$nombre" =~ ^[[:alpha:]]+$ ]];
do
	
	echo "Solo debe contener letras (minusculas o mayusculas)"
	read -p "Ingrese un nombre valido: " nombre
done

echo "El nombre ingresado ($nombre) es correcto :)"
