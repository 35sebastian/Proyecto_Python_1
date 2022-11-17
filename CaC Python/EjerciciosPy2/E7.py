def validarEdad(edad):
  while edad < 1:
    print("%d no es una edad valida!!!" %edad)
    edad = int(input('Hola, Cual es tu edad: '))
  return edad

print("*****************************************")
print("         E J E R C I C I O N° 7")
print("*****************************************")
print()

#ingreso edad
edad = int(input("Hola, cual es tu edad: "))
#evaluo edad sea correcta
edad = validarEdad(edad)

for i in range(edad):
  print(i+1)