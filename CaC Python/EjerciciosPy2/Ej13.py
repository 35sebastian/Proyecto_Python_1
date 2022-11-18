def validarCantidad(cantidad, fruta):
  while cantidad <= 0:
    print("%.2f no es una cantidad valida!!!" %cantidad)
    cantidad = float(input("Ingrese la cantidad (en kg.) de que desea: "))
  return cantidad

print("*****************************************")
print("        E J E R C I C I O N° 13")
print("*****************************************")
print()

FRUTAS = {
    "Banana":80, 
    "Manzana":100, 
    "Pera":50, 
    "Naranja":70
    }

compra = []

fruta = input("Ingrese una fruta (-1 salir): ")
while fruta != '-1':
  if fruta in FRUTAS:
    cantidad = float(input("Ingrese la cantidad (en kg.) de que desea: "))
    cantidad = validarCantidad(cantidad, fruta)
    
    importeTotal = FRUTAS.get(fruta) * cantidad

    compra.append((fruta, cantidad, importeTotal))

  else:
    print("La fruta que busca no esta disponible!")
  
  fruta = input("Ingrese una fruta (-1 salir): ") 

if len(compra) == 0:
  print("Ud. no ha comprado nada")
else:
  print()
  print("SU COMPRA:")
  print("************************************")

  print("Fruta\t\t  Cant.    Total ")
  for i in range(len(compra)):
    print("%s\t\t  %.1f      $ %.2f " %(compra[i][0], compra[i][1], compra[i][2]))
  print("************************************")