#   
#   Mi resolución: 
#    
#   inversion = float(input("Introduce la cantidad a invertir: "))
#   interes= int(input("Introduce el porcentaje de interés anual: "))
#   anos= int(input("Introduce el número de años de inversión: "))
#   
#   '''
#   capital = 0
#   
#   for i in range(anos):
#     inversion = inversion + (inversion * (interes *0.01)) 
#     capital += inversion
#     '''
#   
#   print("el interes obtenido por la inversion en", anos, " años es de: ", inversion*(interes*0.01)*anos)
#

# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años? "))
# for i in range(years):
#     amount = (amount * (1 + interest))
#     print("Capital tras " + str(i+1) + " años: " + str(round(amount)))

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años? "))
print(round(amount * (1 + interest)**years))