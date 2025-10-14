#!/bin/bash

if [[ $# < 1 ]];
then
        echo -e "\nDebes pasar un argumento!!\n"
	exit 1
fi

if [[ ! $1 =~ [[:digit:]]+ ]]; then
	echo -e "\nLa cadena '$1' no contiene ningun numero.\n"
	exit 2
else
	echo -e "\nLa cadena '$1' contiene al menos un numero.\n"
	exit 0
fi
