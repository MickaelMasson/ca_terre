# Nom du programme
"""
Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js

"""

import sys

path_file = sys.argv[0]
path_array = path_file.split("/")
file_name = path_array[-1]

print(file_name)

#la même chose sur une ligne.
#print((sys.argv[0]).split("/")[-1])


"""

1ere version vu par Romain le 14 11 24

import os

nom_fichier = os.path.basename(__file__)
print(nom_fichier)

### Note : 

15min pour faire cet exercice. 
Principal difficulté: 
- comprendre le import os
Ce que j'ai appris : 
- que l'on peut importer des modules pour augmenter les "possibilités"
"""