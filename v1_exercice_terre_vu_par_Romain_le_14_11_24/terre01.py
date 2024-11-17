# Nom du programme
"""
Créez un programme qui affiche son nom de fichier.


Exemples d’utilisation :
$> node exo.js
exo.js

$> node crevette.js
crevette.js

"""

import os

nom_fichier = os.path.basename(__file__)
print(nom_fichier)




### Note : 
"""
15min pour faire cet exercice. 
Principal difficulté: 
- comprendre le import os
Ce que j'ai appris : 
- que l'on peut importer des modules pour augmenter les "possibilités"
"""