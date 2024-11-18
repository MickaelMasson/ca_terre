# Puissance d’un nombre
"""
Créez un programme qui affiche le résultat d’une puissance.

L’exposant ne pourra pas être négatif.

Exemples d’utilisation :
$> node exo.js 2 3
8

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

Fonctions interdites: 
-La fonction pow

"""
import sys

arguments = sys.argv[1:]

if len(arguments) != 2 :
    print("Vous devez saisir deux arguments")
    sys.exit()

base = arguments[0]

exponent = arguments[1]

if not base.lstrip("-").isdigit() :
    print("Votre nombre de base doit etre un entier")
    sys.exit()

base = int(base)

if not exponent.isdigit() :
    print("L'exposant doit etre un entier positif")
    sys.exit()

exponent = int(exponent)

result = base

for i in range(exponent - 1) :
    result = result * base

print(result)