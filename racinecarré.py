# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de carré.")
print("Made by GLMMLT. No license.")
print("")

def carré():
  initial = input("Initial: ")
  result = 10**2
  print("Carré de "+initial+" = "+str(result))

def rc():
  initial = input("Initial: ")
  result = sqrt(int(initial))
  print("Racine carré de "+initial+" = "+str(result))

print("c pour carré")
print("rc pour racine carré")
print("")
answer = input("Que souhaitez-vous calculer: ")
print("")

if(answer == "c"):
  print("Calcul de carré choisi.")
  carré()
elif(answer == "rc"):
  print("Calcul de racine carré choisi.")
  rc()
else:
  print("La réponse donnée est incorrecte.")
