# L’alphabet à partir de

"""
Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle.
"""

lettre = input()
liste_alphabet = [lettre]
    
while liste_alphabet[-1] < "z" :
    lettre = chr(ord(lettre) + 1)
    liste_alphabet.append(lettre)
    
alphabet = "".join(liste_alphabet)
print(alphabet)



### Note : 
"""
40min pour faire cet exercice. 
Principal difficulté: 
- je suis resté bloqué sur une erreur bete avec while, 
  j'imaginais que while tournais jusqu'a ce que la règle soit True, 
  j'avais laissé == au lieu de <
Ce que j'ai appris : 
- while tourne tant que la condition est True
"""