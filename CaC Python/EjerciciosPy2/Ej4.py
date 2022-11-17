#   
#   Mi resolución: 
#    
#       numero= int(input("Ingrese un número:"))
#       
#       cociente = numero%2
#       
#       if cociente == 0 : 
#           print ("El número ingresado es par")
#       else :
#           print ("El número ingresado es impar")
#

print("*****************************************")
print("         E J E R C I C I O N° 4")
print("*****************************************")
print()

nombre = input("Ingrese el nombre de USUARIO: \n")
numero = int(input("Ingrese un numero entero:"))

if numero %2 == 0:
  print("Hola %s, el numero %d es par." %(nombre, numero))
else:
  print("Hola %s, el numero %d es impar." %(nombre, numero))