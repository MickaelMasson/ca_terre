# Racine carrée d’un number
"""
Créez un programme qui affiche la racine carrée d’un entier positif.

Exemples d’utilisation :
$> node exo.js 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

Fonctions interdites: 
-La fonction sqrt

"""
import sys

arguments = sys.argv[1:]

if len(arguments) != 1 :
    print("erreur, vous devez saisir un entier")
    sys.exit()

argument = arguments[0]

if not argument.isdigit() :
    print("erreur, vous devez saisir un entier positif")
    sys.exit()

number = int(argument)

result = 0

for i in range(1,number) :
    if number >= i**2 :
        result += 1
    
print(result)