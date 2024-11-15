# Nombre premier
"""
Créez un programme qui affiche si un nombre est premier ou pas.

Exemples d’utilisation :
$> node exo.js 5
Oui, 5 est un nombre premier.

$> node exo.js 6
Non, 6 n’est pas un nombre premier.

Attention : 0 et 1 ne sont pas des nombres premiers. Gérez les erreurs d’arguments.

"""
argument = input()

if int(argument) > 1 :
    for i in range(2, int(argument) - 1) :
        resultat_division = int(argument) / i 
        if int(resultat_division) * i == int(argument) :
            print(f"Non, {argument} n'est pas un nombre premier.")
            break
    else :
        print(f"Oui, {argument} est un nombre premier.")
else :
    print("Vous devez entrer un nombre positif superieur à 1")


### Note : 
"""
45min pour faire cet exercice. 
Principal difficulté: 
- dans range() ne pas commencer par la valeur 0 car erreur à la 
  premiere division et non plus avec le 1 sinon faux positif.
Ce que j'ai appris : 
- l'option dans range pour définir du départ
"""