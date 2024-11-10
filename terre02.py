# Afficheur d’arguments
"""
Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.


Exemples d’utilisation :
$> ruby exo.rb je suis solide !
je
suis
solide
!
"""
arguments = input("écrivez : je suis solide ! ")
liste_des_arguments = arguments.split(" ")

for i in liste_des_arguments :
    print(i)





### Note : 
"""
12min pour faire cet exercice. 
Principal difficulté: 
- j'utilisais mal split, ma première tentative : " ".split(variable)
Ce que j'ai appris : 
- variable.split(" ")
"""