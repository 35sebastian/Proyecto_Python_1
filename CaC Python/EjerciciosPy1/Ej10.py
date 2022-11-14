#   payaso=450
#   osito=520
#   uclown=int(input("ingrese la cantidad de payasos vendidos:"))
#   ubear=int(input("ingrese la cantidad de ositos vendidos:"))
#   print("la cantidad de peso total de las unidades vendidas es de:", (osito*ubear)+(payaso*uclown), "Grs.") 


unidades_payaso = float(input("Ingrese la cantidad de payasos vendidos: "))
unidades_osito = float(input("Ingrese la cantidad de ositos vendidos: "))
print("Peso total del pedido:", (450 * round(unidades_payaso) + 520 * round(unidades_osito))/1000, "kg ") 