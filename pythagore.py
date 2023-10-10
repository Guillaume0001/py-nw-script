# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de pourcentage.")
print("Made by GLMMLT. No license.")
print("")

def hypoténuse():
  côté1 = input("Premier côté : ")
  côté2 = input("Dexuième côté: ")
  result = sqrt((int(côté1)*int(côté1))+(int(côté2)*int(côté2)))
  print("Hypoténuse = "+str(result))

def côté():
  hypoténuse = input("Hypoténuse: ")
  côté = input("Côté: ")
  result = sqrt((int(hypoténuse)-int(côté)))
  print("Côté = "+str(result))

print("h pour hypoténuse")
print("c pour côté")
print("")
answer = input("Que souhaitez-vous calculer: ")
print("")

if(answer == "h"):
  print("Calcul d'hypoténuse choisi.")
  hypoténuse()
elif(answer == "c"):
  print("Calcul de côté choisi.")
  côté()
else:
  print("La réponse donnée est incorrecte.")
