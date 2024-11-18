# Trié ou pas
"""
Créez un programme qui détermine si une liste d’entiers est triée ou pas.

Exemples d’utilisation :
$> ruby exo.rb 9 8 3
Pas triée !

$> ruby exo.rb 3 8 9 12
Triée !

$> ruby exo.rb “Salut”
erreur.

Fonctions interdites: 
-La fonction sort
"""

import sys

arguments = sys.argv[1:]

if len(arguments) < 2 :
    print("Vous devez saisir au moins 2 arguments")
    sys.exit()

for argument in arguments :
    if not argument.isdigit() :
        print("erreur")
        sys.exit()

for i in range(len(arguments) - 1) :
    if not int(arguments[i]) < int(arguments[(i + 1)]) :
        print("Pas triée !")
        sys.exit()

print("Triée !")