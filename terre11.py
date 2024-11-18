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