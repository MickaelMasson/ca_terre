# Pair ou impair
"""
Créez un programme qui permet de déterminer si l’argument donné 
est un entier pair ou impair..

Exemples d’utilisation :
$> ruby exo.rb 2
pair

$> ruby exo.rb 5
impair

$> ruby exo.rb Bonjour
Tu ne me la mettras pas à l’envers.

$> ruby exo.rb
Tu ne me la mettras pas à l’envers.

Attention : gérez aussi les entiers négatifs.

Fonctions interdites: 
-En Ruby: even? et odd?

"""
nombre = input()
try :
    if int(nombre) < 0 :
        nombre = str(nombre).replace("-","")

    if int(nombre) % 2 == 0 :
        print("pair")
    elif int(nombre) % 2 != 0 :
        print("impair")

except ValueError : 
    print("Tu ne me la mettras pas à l’envers.")

"""
### Note : 

1h45min pour faire cet exercice. 
Principal difficulté: 
- la gestion des nombres négatif, >1h
  1ere idée avec une condition avec isdigit, j'ai mis du temps 
  à me rendre compte que les nombres négatif ne sont pas 
  concidéré comme True par avec isdigit. 
  J'ai essayé abs() sans succes.
  puis la gestion de l'erreur car avant d'utiliser try 
  j'avais une erreur quand je rentrais des lettres
Ce que j'ai appris : 
- isdigit concidère seulement les entiers positifs comme True
- abs() permet de renvoyer la valeur absolu d'un nombre mais 
  je n'ai pas réussi a l'utiliser
- try et except ValueError est très pratique quand on veut 
  éviter les blocages a cause des erreurs
"""