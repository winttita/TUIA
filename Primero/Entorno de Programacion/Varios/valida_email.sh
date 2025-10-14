#!/bin/bash

valida_email(){
	local email="$1"
	while [[ ! "$email" =~ ^[[:alnum:].-_%+]+@[[:alnum:].-]+\.[[:alpha:]]{2,}$ ]];
	do
		read -p "El formato del email ingresado es incorrecto, ingrese uno valido: " email
	done
	echo "El mail indicado ($email) tiene un formato correcto."
}

valida_email "$1"
