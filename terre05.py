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
arguments = input()
liste_arguments = arguments.split(" ")
premier_argument = int(liste_arguments[0])
deuxieme_argument = int(liste_arguments[1])

if premier_argument > deuxieme_argument and deuxieme_argument != 0:
    print(f"résultat: {int((premier_argument / deuxieme_argument))}")
    print(f"reste: {(premier_argument % deuxieme_argument)}")
else :
    print("erreur.")



### Note : 
"""
20min pour faire cet exercice. 
Principal difficulté: 
- l'arrondi de la division, j'ai trouvé floor() 
  mais je devais faire un import, ensuite j'ai 
  pensé a int() beaucoup plus simple
Ce que j'ai appris : 
- floor() pour les arrondi inférieur et 
  découvert ensuite le round() mais pas testé
"""