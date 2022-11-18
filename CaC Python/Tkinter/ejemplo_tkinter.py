from tkinter import * # Tkinter es un paquete o libreria

# Tkinter es el paquete GUI (Graphical User Interface) estándar de Python
# Tkinter proporciona elementos GUI que podemos usar para construir la interfaz:
# Botones, Menús, Campos de Entrada y áreas de visualización

# ¿QUÉ SON LOS WIDGETS EN TKINTER?

# Los widgets son objetos; instancias de clases que representan botones, marcos, etc.
# Cada widget por separado es un ibjeto de Python.
# Al crear un widget, debe pasar su padre como parámetro a la función de creación del widget
# La única excepción es la ventana "raiz",que es la ventana de nivel superior que contendrá todo lo demás y no tiene padre.

raiz = Tk()
# La ventana "raíz" es la ventana de nivel superior que contendrá todo lo demás y no tiene padre.
# El objeto "raíz" es el contenedor base de todos los widgets (objetos: botones, Menús) que forman la interfaz
raiz.title('GUI - Comision 22612')

# ---------- BARRA MENU -----------

# Creación de un toplevel Menú
# Objeto (instancia) barramenú. Le asignamos la Clase Menu() con el parámentro parent "raiz"
barramenu = Menu(raiz)
raiz.config(menu = barramenu)

#---- Botones Barra Menú (barramenu)--

# Instancia de barramenú u objeto submenú de barramenu (padre como parámetro)
# tearoff = 0 (o False) para elimonar separador (línea discontinua)
bbddmenu = Menu(barramenu, tearoff=0)
borrarmenu = Menu(barramenu, tearoff=0)
ayudamenu = Menu(barramenu, tearoff=0)

# Creación de Menú Cascada (Método add_cascade). Pull-down Menú o Menú desplegable
# menu=bbddmenu es una instancia de barramenu o submenú. label es la etiqueta
barramenu.add_cascade(label="BBDD", menu=bbddmenu)
barramenu.add_cascade(label="Limpiar", menu=borrarmenu)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

# Agregar comandos al submenú (Método add_command)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Salir')

borrarmenu.add_command(label='Limpiar')

ayudamenu.add_command(label='Licencia')
ayudamenu.add_command(label='Acerca de...')

# ---------- FRAME CAMPOS -----------

# Los widgets (Objetos) Frame son contenedores para otros widgets
framecampos = Frame(raiz)
framecampos.pack()
# Pack(), separa un Frame de otro dentro de la estructura de la interfaz

# Variables que guardan los contenidos de cada uno de los campos
legajo = StringVar() # Clase StringVar (cadena)
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar() #Clase DoubleVar (flotante)
grado = IntVar() # Clase IntVar() (entero)
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

'''
entero = IntVar() # Declara variable de tipo entera
flotante = DoubleVar() # Declara variable de tipo flotante
cadena = StringVar() # Declara variable de tipo cadena
booleano = BooleanVar() # Declara variable de tipo booleana
'''

# Creación de los Campos

# Entry widget es una caja de texto (text box, campo o field) permite al usuario ingresar cualquier texto de una linea
# Grid Manager facilita la ubicación del widget (objeto: field). Utilizando el método de cuadrícula podemos indicar en qué row y column colocarlos
# Padx: espaciado lateral
# Pady: espaciado vertical
# ipadx,y: espaciado dentro del objeto (widget)

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=1, padx=10, pady=10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=1, padx=10, pady=10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=1, padx=10, pady=10)

grado_input = Entry(framecampos, textvariable=grado)
grado_input.grid(row=3, column=1, padx=10, pady=10)

calificacion_input = Entry(framecampos, textvariable=calificacion)
calificacion_input.grid(row=4, column=1, padx=10, pady=10)

escuela_input = Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=5, column=1, padx=10, pady=10)

localidad_input = Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=6, column=1, padx=10, pady=10)

provincia_input = Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=7, column=1, padx=10, pady=10)

# ---------- LABELS -----------

'''
"STICKY"
    n
  nw  ne
w       e
  sw  se
    s
'''

# Por defecto el widget aparece centrado. Le podemos dar efecto "Sticky"

# El widget de etiqueta (Label()) es un widget estándar de Tkinter que se utiliza para mostrar un texto o una imagen en la pantalla

# Para que el elemento (Objeto etiqueta) se posicione arriba, abajo, a la derecha o izquierda de la celda que lo contiene
# podemos usar el parámetro sticky con las opciones "n" (norte), "s" (sur), "e" (este), etc.

# USAMOS EL MÉTODO DE GRILLA PARA EL POSICIONAMIENTO

legajolabel = Label(framecampos, text="Legajo:")
legajolabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

alumnolabel = Label(framecampos, text="Alumno:")
alumnolabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

emaillabel = Label(framecampos, text="Email:")
emaillabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

gradolabel = Label(framecampos, text="Grado:")
gradolabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

calificacionlabel = Label(framecampos, text="Calificación:")
calificacionlabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

escuelalabel = Label(framecampos, text="Escuela:")
escuelalabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

localidadlabel = Label(framecampos, text="Localidad:")
localidadlabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

provincialabel = Label(framecampos, text="Provincia:")
provincialabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)

# ---------- FRAME BOTONERA -----------

framebotones = Frame(raiz)
framebotones.pack()

boton_crear = Button(framebotones, text="Crear")
boton_crear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

boton_leer = Button(framebotones, text="Leer")
boton_leer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

boton_actualizar = Button(framebotones, text="Actualizar")
boton_actualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

boton_borrar = Button(framebotones, text="Borrar")
boton_borrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

# ---------- FRAME PIE -----------

framecopy = Frame(raiz)
framecopy.pack()
copylabel = Label(framecopy, text="(2022) por Regina Molares para CaC 4.0 - Big Data")
copylabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop() 
# Método para realizar el display, disponible para respuesta del input del usuario hasta que el programa termina