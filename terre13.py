# Trouver la Suisse (lol)
"""
Créez un programme qui prend en paramètre trois entiers et affiche la valeur du milieu.

Exemples d’utilisation :
$> ruby exo.rb 11 40 34
34

$> ruby exo.rb 2 1 3
2

$> ruby exo.rb 2 2 2
erreur.

"""
import sys

arguments = sys.argv[1:]

if len(arguments) != 3 :
    print("erreur vous devez saisir 3 arguments")
    sys.exit()

for argument in arguments :
    if not argument.isdigit():
        print("erreur, vos arguments doivent être des entiers positif")
        sys.exit()

first_number = int(arguments[0])
second_number = int(arguments[1])
third_number = int(arguments[2])

if (first_number == second_number or 
    first_number == third_number or 
    second_number == third_number ) :
    print("erreur, vos valeurs ne peuvent être égale")
    sys.exit()

if (second_number < first_number < third_number or
    third_number < first_number < second_number) : 
    print(first_number)
    sys.exit()
elif (first_number < second_number < third_number or
      third_number < second_number < first_number) :
    print(second_number)
    sys.exit()
else :
    print(third_number)