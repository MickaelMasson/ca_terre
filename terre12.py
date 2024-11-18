# 12 to 24
"""
Créez un programme qui transforme une heure affichée en format 12h en 
une heure affichée au format 24h.

Exemples d’utilisation :
$> ruby exo.rb 11:40PM
23:40

Attention : midi et minuit.

"""
import sys
import re

arguments = sys.argv[1:]

if len(arguments) != 1 :
    print("Erreur, vous devez saisir que un argument")
    sys.exit()

argument = arguments[0]

pattern = r"^(?:[1-9]|[01][0-3]):[0-5]\d(?:AM|am|PM|pm)$"

if not re.match(pattern, argument):
    print(f"{argument} n'est pas un format valide. Vous devez saisir l'heure au format hh:mmAM ou hh:mmPM")
    sys.exit()

colon_index = argument.find(":")
hour = argument[0:colon_index]
minute = argument[colon_index + 1 : colon_index + 3]
period = argument[colon_index + 3 : colon_index + 5]

if period == "AM" or period == "am":
    if hour == "12" :
        if minute == "00" :
            print("minuit")
            sys.exit()
        else :
            print(f"00:{minute}")
            sys.exit()
    else :
        print(f"{hour}:{minute}")
        sys.exit()

if period == "PM" or period == "pm":
    if hour == "12" :
        if minute == "00" :
            print("midi")
            sys.exit()
        else :
            print(f"12:{minute}")
            sys.exit()
    else :
        hour = int(hour)
        print(f"{(hour + 12)}:{minute}")
        sys.exit()



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
15min pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""