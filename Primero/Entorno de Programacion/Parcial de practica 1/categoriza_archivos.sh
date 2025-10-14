#!/bin/bash

mkdir -p txt
mkdir -p doc
mkdir -p ppt
mkdir -p unknown

DIR=$1

get_extension () {
	
	local FILE=$1
	local extension

	case $FILE in
		*.txt)
			echo "El archivo $FILE es un archivo de texto."
			extension="txt"
			;;
		*.doc)
			echo "El archivo $FILE es un archivo de tipo documento."
                        extension="doc"
			;;
		*.ppt)
			echo "El archivo $FILE es un archivo de tipo PowerPoint."
                        extension="ppt"
			;;
		*)
			echo "El archivo $FILE no es de un tipo (txt, doc o ppt)."
                        extension="unknown"
			;;
	esac

	echo "$extension"

}

for FILE in $DIR/*
do

	EXT=$(get_extension $FILE)
	mv $FILE $EXT
done
