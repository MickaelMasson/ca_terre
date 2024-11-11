# 24 to 12
"""
Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.

Exemples d’utilisation :
$> ruby exo.rb 23:40
11:40PM

Attention : midi et minuit.

"""
heure24 = input()
liste_h_m = heure24.split(":")
heure = liste_h_m[0]
minute = liste_h_m[1]

if heure24 == "00:00" :
    print("12:00AM")
elif heure24 == "12:00" :
    print("12:00PM")
elif heure == "00" :
    print(f"12:{minute}AM")
elif int(heure) > 0 and int(heure) < 12 :
    print(f"{heure}:{minute}AM")
elif heure == "12" :
    print(f"12:{minute}PM")
elif int(heure) > 12 and int(heure) < 24 :
    print(f"{(int(heure) - 12)}:{minute}PM")

### Note : 
"""
25min pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""