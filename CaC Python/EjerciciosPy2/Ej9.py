print("*****************************************")
print("         E J E R C I C I O N° 9")
print("*****************************************")
print()

palabra = input("Ingrese una palabra: ")
largoPalabra = len(palabra)
while largoPalabra != 0:
  print(palabra[largoPalabra-1])
  largoPalabra -= 1
