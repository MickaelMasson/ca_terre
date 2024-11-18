# Divisions
"""
Créez un programme qui affiche le résultat et le reste d’une division 
entre deux nombres.

Exemples d’utilisation :
$> python exo.py 5 2
résultat: 2
reste: 1

$> python exo.py 10 0
erreur.

$> python exo.py 3 5
erreur.

"""

import sys

arguments = sys.argv[1:]

if len(arguments) != 2 :
    print("erreur, vous devez saisir deux arguments")
    sys.exit()

for argument in arguments :
    if not argument.isdigit() :
        print("erreur, vos argmuents doivent être des entiers positif")
        sys.exit()

dividend = int(arguments[0])

divider = int(arguments[1])

if divider == 0 :
    print("erreur, il est imposible de diviser par zéro")
    sys.exit()

if dividend < divider:
    print("erreur, le diviseur ne peut pas est supérieur au dividende")
    sys.exit()

float_result = dividend / divider

str_result = str(float_result)

point_index = str_result.find(".")

result = str_result[0:point_index]

rest = dividend % divider

print(f"resultat: {result}")
print(f"reste: {rest}")

"""
premier_argument = int(arguments[0])
deuxieme_argument = int(arguments[1])

if premier_argument > deuxieme_argument and deuxieme_argument != 0:
    print(f"résultat: {int((premier_argument / deuxieme_argument))}")
    print(f"reste: {(premier_argument % deuxieme_argument)}")
else :
    print("erreur.")



### Note : 

20min pour faire cet exercice. 
Principal difficulté: 
- l'arrondi de la division, j'ai trouvé floor() 
  mais je devais faire un import, ensuite j'ai 
  pensé a int() beaucoup plus simple
Ce que j'ai appris : 
- floor() pour les arrondi inférieur et 
  découvert ensuite le round() mais pas testé
"""