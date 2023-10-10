# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de vitesse.")
print("Made by GLMMLT. No license.")
print("")

def vitesse():
  d = input("Distance: ")
  t = input("Temps: ")
  v=int(d)/int(t)
  print("Vitesse: "+str(v))

def distance():
  v = input("Vitesse: ")
  t = input("Temps: ")
  d=int(v)*int(t)
  print("Distance: "+str(d))

def temps():
  d = input("Distance: ")
  v = input("Vitesse: ")
  t=int(d)/int(v)
  print("Temps: "+str(t))

print("v pour vitesse")
print("d pour distance")
print("t pour temps")
print("")
answer = input("Que souhaitez-vous calculer: ")
print("")

if(answer == "v"):
  print("Calcul de vitesse choisi.")
  vitesse()
elif(answer == "d"):
  print("Calcul de distance choisi.")
  distance()
elif(answer == "t"):
  print("Calcul de temps choisi.")
  temps()
else:
  print("La réponse donnée est incorrecte.")
