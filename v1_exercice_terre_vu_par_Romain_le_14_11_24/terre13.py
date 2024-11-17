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
arguments = input()

liste_arguments = arguments.split(" ")
premier_argument = liste_arguments[0]
deuxieme_argument = liste_arguments[1]
troisieme_argument = liste_arguments[2]


if ((int(premier_argument) > int(deuxieme_argument) and int(premier_argument) < int(troisieme_argument)) 
    or (int(premier_argument) < int(deuxieme_argument) and int(premier_argument) > int(troisieme_argument))):
    print(premier_argument) 

if ((int(deuxieme_argument) > int(premier_argument) and int(deuxieme_argument) < int(troisieme_argument)) 
    or (int(deuxieme_argument) < int(premier_argument) and int(deuxieme_argument) > int(troisieme_argument))):
    print(deuxieme_argument)
    
if ((int(troisieme_argument) > int(deuxieme_argument) and int(troisieme_argument) < int(premier_argument)) 
    or (int(troisieme_argument) < int(deuxieme_argument) and int(troisieme_argument) > int(premier_argument))):
    print(troisieme_argument)


### Note : 
"""
15min pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""