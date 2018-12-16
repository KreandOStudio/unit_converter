#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

seguimos = True
milla = 1.609
kms = None
conv = None

print "Bienvenidos al Conversor de Unidades! "
print "Este programa convierte los kilometros introducidos a millas."

while seguimos:
    try:
        kms = float(raw_input("Introduzca el número de Kilómetros a convertir (ejemplo: 24.3): "))
        if kms >= 0:
            conv = kms / milla
            print "El resultado de la conversión es {} millas.".format(conv)
            correcto = True
            while correcto:
                pregunta = raw_input("¿Desea hacer otra conversión? (S/N): ")[0]
                pregunta = pregunta.lower()
                # print pregunta.upper(): Pone en mayusculas.
                # print pregunta.lower(): Pone en minusculas.
                #if pregunta == "n" or pregunta == "N": # or pregunta == "no" or pregunta =="NO" or pregunta == "No" or pregunta == "nO":
                if pregunta == "n":
                    seguimos = False
                    correcto = seguimos
                    print "Muchas gracias por usar el Conversor de Unidades."
                elif pregunta == "s" or pregunta == "S":
                    correcto = False
                else:
                    print "Disculpe, no ha introducido una opción validad"
        else:
            print "NO estan permitidos los numeros negativos."
    except ValueError:
        print "Por favor, introduzca solo números como por ejemplo 26.4."
