def evaluoLargoLetra(letra):
  while len(letra) > 1:
    print("El largo es incorrecto, solo se permite una letra.")
    letra = input("Ingrese la letra a buscar: ")

  return letra

print("*****************************************")
print("        E J E R C I C I O N° 10")
print("*****************************************")
print()
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese la letra a buscar: ")
letra = evaluoLargoLetra(letra)

largoPalabra = len(palabra)
contador = 0

for i in range(largoPalabra):
  if palabra[i] == letra:
    contador +=1
  
if contador > 0:
  print("Respuesta: La palabra '%s' tiene %d veces la letra '%s'" %(palabra, contador, letra))
else:
  print("Respuesta: No se encotro la letra '%s' en la palabra '%s'" %(letra, palabra))
