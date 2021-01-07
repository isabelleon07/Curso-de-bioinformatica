#Ejecicio ciclo while para programacion python

#escribe la inicial para encontrar el nucleótido


nucleotide = ""

#Iniciamos el ciclo
while (nucleotide != "X"):
    
  nucleotide = input("Escribe X para salir,  nucleotido A, C, T, G :")
  print(nucleotide)

  if (nucleotide == "A"):
    print ("ADENINA")
  elif (nucleotide == "C"):
    print ("CITOSINA")
  elif (nucleotide == "T"):
    print ("TIMINA")
  elif (nucleotide == "G"):
    print("GUANINA")
  elif (nucleotide == "X"):
    print("Bye..")
  else:
    print("ERROR en input")