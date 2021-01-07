
#Practica de ejercicios basicos python


adn = ""

#Inicio de ejercicio python
f = open("adn.txt", "r")
for x in f:
  adn = adn + x

adn = adn.strip()

n = len(adn)
print(" adn length = ", n)

for i in range(0, n):
  print(i+1,  adn[i])