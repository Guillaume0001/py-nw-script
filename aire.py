# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de vitesse.")
print("Made by GLMMLT. No license.")
print("")

def cr():
  côté1 = input("Premier côté: ")
  côté2 = input("Deuxième côté: ")
  result = côté1+côté2
  print("Aire = "+str(result))

def tr():
  côté1 = input("Premier côté: ")
  côté2 = input("Deuxième côté: ")
  result = (côté1+côté2)/2
  print("Aire = "+str(result))

def ce():
  rayon = input("Rayon: ")
  result = pi*sqr(rayon)
  print("Aire = "+str(result))

def dc():
  rayon = input("Rayon: ")
  result = (pi*sqr(rayon))/2
  print("Aire = "+str(result))

print("cr pour carré et rectangle")
print("tr pour triangle rectangle")
print("ce pour cercle")
print("dc pour demi-cercle")
print("")
answer = input("Que souhaitez-vous calculer: ")
print("")

if(answer == "cr"):
  print("Calcul de carré et rectangle choisi.")
  cr()
elif(answer == "tr"):
  print("Calcul de triangle rectangle choisi.")
  tr()
elif(answer == "ce"):
  print("Calcul de cercle choisi.")
  ce()
elif(answer == "dc"):
  print("Calcul de demi-cercle choisi.")
  dc()
else:
  print("La réponse donnée est incorrecte.")
