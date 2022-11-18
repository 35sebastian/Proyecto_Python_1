def validarNumeroMayorACero(numero):
  while numero <= 0:
    print("%d no es valido. Debe ingresar un credito mayor a 0" %numero)
    numero = int(input("Ingrese su credito: "))
  return numero

print("*****************************************")
print("        E J E R C I C I O N° 14")
print("*****************************************")
print()

creditos = {}


materia = input("Ingrese la materia (-1 Salir): ")

while materia != '-1':
  credito = int(input("Ingrese su credito: "))
  credito = validarNumeroMayorACero(credito)
  creditos[materia] = credito

  materia = input("Ingrese la materia (-1 Salir): ")

print()
for materia in creditos:
  if creditos[materia] == 1:
    print("La asignatura '%s' tiene %d credito." %(materia, creditos[materia]))  
  else:
    print("La asignatura '%s' tiene %d creditos." %(materia, creditos[materia]))
