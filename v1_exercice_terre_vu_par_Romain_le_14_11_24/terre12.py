# 12 to 24
"""
Créez un programme qui transforme une heure affichée en format 12h en 
une heure affichée au format 24h.

Exemples d’utilisation :
$> ruby exo.rb 11:40PM
23:40

Attention : midi et minuit.

"""

heure12 = input()
liste_h_m = heure12.split(":")
heure = liste_h_m[0]
minute_lettres = liste_h_m[1]
minute = minute_lettres[0:2]
lettres = minute_lettres[2:]

if heure12 == "12:00AM" :
    print("00:00 - minuit")
elif heure12 == "12:00PM" :
    print("12:00 - midi")
elif heure == "12" and lettres == "AM":
    print(f"00:{minute}")
elif (int(heure) > 0 and int(heure) < 12) and lettres == "AM":
    print(f"{heure}:{minute}")
elif heure == "12" and lettres == "PM":
    print(f"13:{minute}")
elif (int(heure) > 0 and int(heure) < 12) and lettres == "PM"  :
    print(f"{(int(heure) + 12)}:{minute}")



### Note : 
"""
15min pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""