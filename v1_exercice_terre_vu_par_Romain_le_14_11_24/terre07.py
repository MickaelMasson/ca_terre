# Taille d’une chaîne
"""
Créez un programme qui affiche le nombre de caractères d’une chaîne de 
caractères passée en argument.

Exemples d’utilisation :
$> python exo.py “Hello world!”
12

$> python exo.py
erreur.

$> python exo.py “Bonjour” “Aurevoir”
erreur.

$> python exo.py 10
erreur.

Fonctions interdites: 
-La fonction length
-La fonction size
"""


chaine = input()
compteur_de_caractere = -2

if ((chaine.find('"') == -1 and chaine.find("'") == -1) 
    or (chaine.count("'") != 2 and chaine.count('"') != 2)) :
    print("erreur.")

else :
    while chaine != "" :
        chaine = chaine[:-1]
        compteur_de_caractere += 1
    
    print(compteur_de_caractere)
    
    

### Note : 
"""
45min pour faire cet exercice. 
Principal difficulté: 
- a cause d'une erreur de frappe, oublie du - dans [:-1], 
j'ai eu besoin de 30min pour trouver l'erreur
Ce que j'ai appris : 
- mettre des () pour faire un saut de ligne dans une instruction
"""