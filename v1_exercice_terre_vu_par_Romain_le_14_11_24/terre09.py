# Racine carrée d’un nombre
"""
Créez un programme qui affiche la racine carrée d’un entier positif.

Exemples d’utilisation :
$> node exo.js 9
3

Attention : je compte sur vous pour gérer les potentielles erreurs d’arguments.

Fonctions interdites: 
-La fonction sqrt

"""

argument = input()

if not argument.isdigit() :
    print("erreur.")
elif int(argument) < 0 :
    print("ça doit etre un entier positif")
else :
    i = 1
    while int(i)**2 < int(argument):
        i += 1
    if int(i)**2 == int(argument) :
        print(i)
    else :
        print(f"Ce résultat est arrondi à l'inférieur : {(i - 1)} ")


### Note : 
"""
40min pour faire cet exercice. 
Principal difficulté: 
- Je ne comprend pas pourquoi je suis obligé de mettre i-1 a la fin 
  alors que dans la boucle j'ai bien mit strictement inférieur
Ce que j'ai appris : 
- le carré d'un nombre se fait avec **2 (puissance 2)
"""