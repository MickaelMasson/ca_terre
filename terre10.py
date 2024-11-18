# Nombre premier
"""
Créez un programme qui affiche si un number est premier ou pas.

Exemples d’utilisation :
$> node exo.js 5
Oui, 5 est un number premier.

$> node exo.js 6
Non, 6 n’est pas un number premier.

Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.

"""
import sys

arguments = sys.argv[1:]

if len(arguments) != 1 :
    print("erreur, vous devez saisir un seul argument")
    sys.exit()

argument = arguments[0]

if not argument.isdigit() :
    print("Vous devez saisir un nombre entier positif")
    sys.exit()

number = int(argument)

if number < 2 :
    print("0 et 1 ne sont pas des nombres premiers")
    sys.exit()

for i in range(2, number):
    if number % i == 0 :
        print(f"Non, {number} n'est pas un nombre premier")
        sys.exit()

print(f"Oui, {number} est un nombre premier.")