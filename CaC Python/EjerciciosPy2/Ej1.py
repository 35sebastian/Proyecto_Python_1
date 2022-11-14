#   
#   Mi resolución: 
#    
#   edad= int(input("Ingrese su edad:"))
#   if edad < 18:
#       print("Según tu edad eres menor de edad")
#   else:
#       print("Según tu edad eres mayor de edad")
#       

def validarEdad(edad):
  while edad < 1:
    print("%d no es una edad valida!!!" %edad)
    edad = int(input('Hola, Cual es tu edad: '))
  return edad

print("*****************************************")
print("         E J E R C I C I O N° 1")
print("*****************************************")

usuario = input('Cual es tu usuario: ')

edad = int(input('Hola %s, Cual es tu edad: ' %usuario))
edad = validarEdad(edad)

if edad >= 18:
  print("Tu usuario es %s y tu edad es %d, por lo tanto sos MAYOR de edad" %(usuario, edad))
else:
  print("El usuario es %s y tu edad es %d, por lo tanto sos MENOR de edad" %(usuario, edad))


