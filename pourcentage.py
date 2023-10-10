# Normaly work for all NUMWORKS calculator.
# Not affilied with NUMWORKS company.

from math import *

print("Calcul de pourcentage.")
print("Made by GLMMLT. No license.")
print("")

def augmentation():
  initial = input("Initial: ")
  pourcentage = input("Pourcentage: ")
  result = int(initial)*(1+int(pourcentage)/100)
  difference = result-int(initial)
  print("Nouvel intial: "+str(result))
  print("Différence: "+str(difference))
  
def reduction():
  initial = input("Initial: ")
  pourcentage = input("Pourcentage: ")
  result = int(initial)*(1-int(pourcentage)/100)
  difference = result-int(initial)
  print("Nouvel initial: "+str(result))
  print("Difference: "+str(difference))

def pourcentage():
  initial1 = input("Premier intial: ")
  initial2 = input("Deuxième initial: ")
  result = int(initial1)/int(initial2)*100
  print("Pourcentage: "+str(result)+"%")
  
print("a pour calculer une augmentation")
print("r pour calculer une diminution")
print("p pour calculer un pourcentage")
print("")
answer = input("Que souhaitez-vous calculer: ")
print("")

if(answer == "a"):
  print("Calcul d'augmentation choisi.")
  augmentation()
elif(answer == "r"):
  print("Calcul de diminution choisi.")
  reduction()
elif(answer == "p"):
  print("Calcul de pourcentage choisi.")
  pourcentage()
else:
  print("La réponse donnée est incorrecte.")
