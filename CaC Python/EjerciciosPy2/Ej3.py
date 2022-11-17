#   
#   Mi resolución: 
#    
#       a= int(input("Ingrese el dividendo:"))
#       b= int(input("Ingrese el divisor:"))
#       
#       if b != 0:
#           print (a/b)
#       else:
#           print ("No es posible dividir por cero!")
#       

def validarNumeroNoCero(numero):
  while numero == 0:
    print("%d no es valido. El divisor NO puede ser cero." %numero)
    numero = float(input("Ingrese el 2do numero: "))
  return numero

print("*****************************************")
print("         E J E R C I C I O N° 3")
print("*****************************************")
print()

nombre = input("Ingrese el nombre de USUARIO: \n")
print("Hola %s, vamos a hacer una division.\nA continuacion necesito ingreses 2 numeros:" %nombre)

dividendo = float(input("Ingrese el 1er numero: "))
divisor = float(input("Ingrese el 2do numero: "))
divisor = validarNumeroNoCero(divisor)

division = dividendo / divisor

print("%s, el resultado de la divion entre %.2f y %.2f es %.2f" %(nombre, dividendo, divisor, division))