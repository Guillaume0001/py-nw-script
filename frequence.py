# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de vitesse.")
print("Made by GLMMLT. No license.")
print("")

def freq(t):
  r = 1/t
  print("Frequence: "+str(r)+"Hz")
  
t = input("Temps: ")

freq(int(t))
