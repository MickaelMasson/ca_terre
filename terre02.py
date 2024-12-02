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

import sys

"""print(sys.argv) #['/home/mickael/Documents/github/ca_terre/terre02.py', 'je', 'suis', 'un']
print(sys.argv[1:]) #['je', 'suis', 'un']
print(sys.argv[:1]) #['/home/mickael/Documents/github/ca_terre/terre02.py']
print(sys.argv[-1:]) #['un']
print(sys.argv[:-1]) #['/home/mickael/Documents/github/ca_terre/terre02.py', 'je', 'suis']
print(sys.argv[1::2]) #['je', 'un']
print(sys.argv[0]) #/home/mickael/Documents/github/ca_terre/terre02.py"""


if len(sys.argv) > 1:
    for argument in sys.argv[1:] :
        print(argument)
else:
    print("aucun argument")



"""
arguments = input("écrivez : je suis solide ! ")
liste_des_arguments = arguments.split(" ")

for i in liste_des_arguments :
    print(i)


### Note : 

12min pour faire cet exercice. 
Principal difficulté: 
- j'utilisais mal split, ma première tentative : " ".split(variable)
Ce que j'ai appris : 
- variable.split(" ")
"""