# Inverser une chaîne
"""
Créez un programme qui affiche l’inverse de la chaîne de caractères 
donnée en argument.

Exemples d’utilisation :
$> node exo.js “Hello world!”
!dlrow olleH

$> node exo.js “lehciM”
Michel

Attention : je compte sur vous pour gérer les potentielles 
erreurs d’arguments.

Fonctions interdites: 
-La fonction reverse
"""

import sys

arguments = sys.argv[1:]

if len(arguments) != 1 :
    print("erreur, vous devez saisir au moins 1 arguments")
    sys.exit()

argument = arguments[0]
reversed_argument = ""

for i in range(len(argument) -1, -1, -1) :
    reversed_argument += argument[i]
    #print(i)

print(reversed_argument)