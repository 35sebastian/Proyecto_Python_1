def validarEdad(edad):
  while edad < 1:
    print("%d no es una edad valida!!!" %edad)
    edad = int(input('Hola, Cual es tu edad: '))
  return edad

print("*****************************************")
print("         E J E R C I C I O N° 6")
print("*****************************************")
print()

#ingreso edad
edad = int(input("Para ingresar debes decirme su edad: "))
#evaluo edad sea correcta
edad = validarEdad(edad)

#valido la edad
if edad < 4:
  print("Tu edad es %d por lo que entras gratis!!!" %edad)
elif edad >= 4 and edad <=17:
  print("Tu edad es %d, todavia no sos mayor de edad por lo que pagas $1500!!!" %edad)
else :
  print("Tu edad es %d, ya sos mayor de edad por lo que pagas $3000!!!" %edad)
