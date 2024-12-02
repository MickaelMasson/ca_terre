# L'alphabet 
"""
Créez un programme qui affiche l’alphabet en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py
abcdefghijklmnopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle."""

alphabet_list = []

#97 Valeur décimal de "a", 122 Valeur décimal de "z" 
for letter in range(97, 123):
    alphabet_list.append(chr(letter))

alphabet_list.append("\n")

print("".join(alphabet_list))



"""
Première version de mon exercice vu par Romain le 14 11 24

liste_alphabet = []
lettre = "a"

for i in range(26) :
    liste_alphabet.append(chr(ord(lettre) + i))

alphabet = "".join(liste_alphabet)
print(alphabet + "\\n")


### Note : 

50min pour faire cet exercice. 
Principal difficulté: 
- comment incrémenter les lettres de l'alphabet.
Ce que j'ai appris : 
- ord() pour récupérer le code le la lettre
- chr() converti le code de la lettre en lettre
- "\\n" pour un retour à la ligne
"""