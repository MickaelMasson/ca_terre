# 24 to 12
"""
Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.

Exemples d’utilisation :
$> ruby exo.rb 23:40
11:40PM

Attention : midi et minuit.

"""
import sys

arguments = sys.argv[1:]

error = "Vous devez saisir l'heure au format HH:MM"
if len(arguments) != 1 :
    print(f"{error} erreur 1")
    sys.exit()

argument = arguments[0]

colon_index = argument.find(":")

if colon_index == -1 :
    print(f"{error} erreur 2")
    sys.exit()

if len(argument) != 5 :
    print(f"{error} erreur 3")
    sys.exit()

hour = argument[:colon_index]

if not hour.isdigit() :
    print(f"{error} erreur 4")
    sys.exit()

hour = int(hour)

if not 0 <= hour < 24 :
    print(f"{error} erreur 5")
    sys.exit()

minute = argument[colon_index + 1:]

if not minute.isdigit() :
    print(f"{error} erreur 6")
    sys.exit()

minute = int(minute)

if not 0 <= minute < 60 :
    print(f"{error} erreur 7")
    sys.exit()

minute = str(minute).zfill(2)

if hour < 12 :
    if hour == 0 :
        print(f"12:{minute}AM")
        sys.exit()
    else :
        print(f"{hour}:{minute}AM")
        sys.exit()

if hour >= 12 :
    if hour == 12 :
        print(f"12:{minute}PM")
        sys.exit()
    else :
        hour = hour - 12
        print(f"{hour}:{minute}PM")
        sys.exit()

"""
heure24 = input()
period = heure24.split(":")
heure = period[0]
minute = period[1]

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

25min pour faire cet exercice. 
Principal difficulté: 
- 
Ce que j'ai appris : 
- 
"""