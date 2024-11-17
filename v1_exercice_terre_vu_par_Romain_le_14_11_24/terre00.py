# L'alphabet 
"""
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle."""


liste_alphabet = []
lettre = "a"

for i in range(26) :
    liste_alphabet.append(chr(ord(lettre) + i))

alphabet = "".join(liste_alphabet)
print(alphabet + "\n")



### Note : 
"""
50min pour faire cet exercice. 
Principal difficulté: 
- comment incrémenter les lettres de l'alphabet.
Ce que j'ai appris : 
- ord() pour récupérer le code le la lettre
- chr() converti le code de la lettre en lettre
- "\n" pour un retour à la ligne
"""