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
period = (argument[colon_index + 3 : colon_index + 5]).upper()

#print(period)

if period == "AM" :
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

if period == "PM" :
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