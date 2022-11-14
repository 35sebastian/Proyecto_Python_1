


inversion = int(input("Introduce la cantidad a invertir: "))
interes= int(input("Introduce el porcentaje de interés anual: "))
anos= int(input("Introduce el número de años de inversión: "))

capital = 0

for i in range(anos):
  inversion = inversion + (inversion * (interes *0.01)) 
  capital += inversion

print("el interes obtenido por la inversion en", anos, " años es de: ", capital*(interes*0.01)*anos, "%")