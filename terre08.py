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

base_number = arguments[0]

exponent = arguments[1]

if not base_number.lstrip("-").isdigit() :
    print("Votre nombre de base doit etre un entier")
    sys.exit()

base_number = int(base_number)

if not exponent.isdigit() :
    print("L'exposant doit etre un entier positif")
    sys.exit()

exponent = int(exponent)

result = base_number

for times in range(exponent - 1) :
    result = result * base_number

print(result)

"""
try :
    arguments = input()
    liste_arguments = arguments.split(" ")
    premier_argument = int(liste_arguments[0])
    deuxieme_argument = int(liste_arguments[1])
    resultat = premier_argument

    if deuxieme_argument == 0 :        
        print(resultat)
    
    for i in range(int(deuxieme_argument - 1)) :
        resultat = resultat * premier_argument
    print(resultat)
       
except :
    print("erreur.")


### Note : 

40min pour faire cet exercice. 
Principal difficulté: 
- gestion des erreur et erreur bete de x^0 = x
Ce que j'ai appris : 
- la gestion de TOUTES les erreurs avec juste try et except
"""