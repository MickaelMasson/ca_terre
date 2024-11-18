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

for i in argument[::-1] :
    reverse_argument = ""
    reverse_argument = argument[:-1]

print(reverse_argument)

"""
mots = input()
liste_lettre = []

while len(mots) > 0 :
    derniere_lettre = mots[-1]
    liste_lettre.append(derniere_lettre)
    mots = mots[:-1]

mots_a_l_envers = "".join(liste_lettre)
print(mots_a_l_envers)


### Note : 

20min pour faire cet exercice. 
Principal difficulté: 
- j'avais oublié les : dans mots = mots[:-1], 
  du coup ça n'enlevais pas la dernière lettre 
  et faisait une boucle infini.
Ce que j'ai appris : 
- la différence entre [-1] et [:-1]
"""