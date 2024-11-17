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

arguments = input()
liste_arguments = arguments.split(" ")
if arguments.replace(" ", "").isdigit() :
    i = 0
    for i in range(len(liste_arguments) - 1) : 
        if liste_arguments[int(i)] < liste_arguments[int(i) + 1] :
            i += 1
    if i + 1 == len(liste_arguments) :
        print("Triée !")
    else :
        print("Pas trié !")     
else :
    print("erreur.")


### Note : 
"""
1h50 pour faire cet exercice. 
Principal difficulté: 
- comment diférencier des chiffres avec des espaces et 
  trouver la methode de l'index pour naviguer dans la liste
Ce que j'ai appris : 
- j'ai compris que le .isdigit renvoie True orr False
"""