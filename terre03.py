# L’alphabet à partir de

"""
Créez un programme qui affiche l’alphabet à partir de la lettre donnée en arguments en lettres minuscules suivi d’un retour à la ligne.

Exemples d’utilisation :
$> python exo.py n
nopqrstuvwxyz
$>

Attention : votre programme devra utiliser une boucle.
"""

import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
   print("Erreur, vous devez saisir une seule lettre ; a-z")
   sys.exit() # !!! bien utiliser sys.exit() et pas exit()

argument = arguments[0]

if len(argument) != 1:
   print("Erreur, vous devez saisir une seule lettre ; a-z")
   sys.exit() # !!! bien utiliser sys.exit() et pas exit()

start_letter = argument

if not start_letter.isalpha():
  print("Erreur, vous devez saisir une seule lettre ; a-z")
  sys.exit() # !!! bien utiliser sys.exit() et pas exit()

start_ascii_letter = ord(start_letter) #ord() obtenir le code ASCII d'un caractère,
alphabet_list = []

for letter in range(start_ascii_letter, 123): #122 Valeur décimal de "z"
    alphabet_list.append(chr(letter))

print("".join(alphabet_list))


"""
lettre = input()
liste_alphabet = [lettre]
    
while liste_alphabet[-1] < "z" :
    lettre = chr(ord(lettre) + 1)
    liste_alphabet.append(lettre)
    
alphabet = "".join(liste_alphabet)
print(alphabet)



### Note : 

40min pour faire cet exercice. 
Principal difficulté: 
- je suis resté bloqué sur une erreur bete avec while, 
  j'imaginais que while tournais jusqu'a ce que la règle soit True, 
  j'avais laissé == au lieu de <
Ce que j'ai appris : 
- while tourne tant que la condition est True
"""