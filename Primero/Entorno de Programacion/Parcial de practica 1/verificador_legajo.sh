#!/bin/bash

if [[ $# -ne 1 ]];then

	echo "Uso: $0 <legajo>."
	exit 1
fi	

legajo=$1

if [[ ! "$legajo" =~ ^[A-Z]{1}-[0-9]{4}/[0-9]{1}$ ]]; then
	echo -e "\nEl legajo ingresado no coincide con el formato L-NNNN/N.\n"
else
	echo -e "\nEl formato del legajo es correcto :)\n"
fi
