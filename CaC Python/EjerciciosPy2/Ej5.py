'''
Evalua el que el valor ingresado de desempeño sea correcto correspondiente a las constantes.
'''
def evaluarDesempeño():
    #constantes
    INACEPTABLE = 0.0
    ACEPTABLE = 0.4
    MERITORIO1 = 0.6
    MERITORIO2 = 0.8
    MERITORIO3 = 1.0

    valor = float(input("Ingrese el desempeño del Empleado: "))
    
    while valor != INACEPTABLE and valor != ACEPTABLE and valor != MERITORIO1 and valor != MERITORIO2 and valor != MERITORIO3:
        print("El valor de desempeño no es valido.")
        print("Valores validos: %.1f - %.1f - %.1f - %.1f - %.1f." %(INACEPTABLE, ACEPTABLE, MERITORIO1, MERITORIO2, MERITORIO3))
        valor = float(input("Ingrese el desempeño del Empleado: "))
        
    return valor

'''
Ingresa los valores de Empleado + Desempeño hasta que el usuario coloca -1 en el nombre para salir.
'''
def entradaDatos():

  id = 1
  empleados = []
  importe = 0
  
  nombre = input("Ingrese Nombre del Empleado %d (-1 fin de ingresos): " %id) 
  while nombre != "-1":   
    desempeno = evaluarDesempeño()
    empleados.append([id, nombre, desempeno,importe])

    id += 1
    nombre = input("Ingrese Nombre del Empleado %d (-1 fin de ingresos): " %id) 

  return empleados


#constante
MONTOBASE = 100000

print("*****************************************")
print("         E J E R C I C I O N° 5")
print("*****************************************")
print()

#cargo los datos de empleados
empleados = entradaDatos()
print(len(empleados))

#evaluo desempeño y guardo valor de bono
for i in range(len(empleados)):
    empleados[i][3] = MONTOBASE + MONTOBASE * empleados[i][2]

#imprime la tabla completa:
print("Tabla de desempeño:")
print("************************************************************************")
print("ID\t USUARIO\t Desempeño (%)\t Monto + Desempeño")
for i in range(len(empleados)):
  print("%d\t %s\t\t %.1f\t\t $ %.2f" %(empleados[i][0], empleados[i][1], empleados[i][2], empleados[i][3]))
print("************************************************************************")