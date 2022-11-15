from getpass import getpass as gp   # Con la librería getpass conseguimos que la contraseña pueda permanecer oculta mientras es ingresada.

nombre = input("Ingrese el nombre de USUARIO: \n")
print("Ingrese la CONTRASEÑA: \t")
contrasena = gp()

print("*****************************************")
print("         E J E R C I C I O N° 2")
print("*****************************************")
print()
nombreNuevo = input("Ingrese el nombre de USUARIO: \n")
print("Ingrese la CONTRASEÑA: \t")
contrasenaNueva = gp()

if nombre == nombreNuevo and contrasena == contrasenaNueva:
  print("Bienvenido %s, te has logueado exitosamente." %nombreNuevo)
else:
  print("Los datos ingresados son incorrectos.")

#       
#       nombre = input("Ingrese el nombre de USUARIO: \n")
#       contrasena = input("Ingrese la CONTRASEÑA: \t")
#       
#       
#       print("*****************************************")
#       print("         E J E R C I C I O N° 2")
#       print("*****************************************")
#       print()
#       nombreNuevo = input("Ingrese el nombre de USUARIO: \n")
#       contrasenaNueva = input("Ingrese la CONTRASEÑA: \t")
#       
#       
#       if nombre == nombreNuevo and contrasena == contrasenaNueva:
#         print("Bienvenido %s, te has logueado exitosamente." %nombreNuevo)
#       else:
#         print("Los datos ingresados son incorrectos.")
#       
#       