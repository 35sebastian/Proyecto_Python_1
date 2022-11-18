print("*****************************************")
print("        E J E R C I C I O N° 12")
print("*****************************************")
print()

materias = []

materia = input("Ingrese una materia (-1 salir): ")
while materia != '-1':
  materias.append(materia)
  materia = input("Ingrese una materia (-1 salir): ")

print()
if len(materias) > 0:
  for i in range(len(materias)):
    print("Yo estudio %s." %materias[i])
else:
  print("Yo no estudio nada.")