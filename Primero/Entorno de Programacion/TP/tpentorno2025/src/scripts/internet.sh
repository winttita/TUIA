#!/bin/bash

# Este script simplemente debe chequear que haya conexión a internet.
# Asegúrese de retornar un valor de salida acorde a la situación.
# Puede que necesite modificar el archivo Dockerfile.

clear

echo "Verificando conexión a internet..."

INTERNET_RESULTADO=$(ping -c 3 google.com | grep "100% packet loss") 


# Verificación de conexión a internet
echo "---------------"

if [ "$INTERNET_RESULTADO" = '' ]; then
    echo "Conexión establecida"
else
    echo "Error: Verifique la conexión a internet"
    exit 1
fi

echo "---------------"
