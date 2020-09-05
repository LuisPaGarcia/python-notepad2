from tkinter import *
from tkinter import filedialog
from io import open
from PIL import ImageTk, Image

window = Tk()
title = " Bloc de Notas"
window.title(title)
errores = ""
#window.geometry("400x600")

# window.iconbitmap(r"C:\Users\aleja\Desktop\ImagenesPrograma\Iconos\bloc_de_notas.ico")

url_file = ""


# Funciones

def new_file():
    global url_file
    text.delete(1.0, "end")  # Borramos desde el caracter 1 hasta el ultimo
    url_file = ""
    window.title(url_file + title)

def open_file():
    global url_file
    url_file = filedialog.askopenfilename(
        initialdir=".",
        filetypes=(("Archivos de texto", "*.txt"), ("all files", "*.*")),
        title="Abrir Archivo"
    )
        # con esto ya tenemos la ruta actual del archivo abierto
    # title: con lo que estableceremos el titulo de nuestro cuadro de dialogo
    if url_file != "":  # si abrimos algo es porque nuestra url no esta vacia
        file = open(url_file, "r")  # r que sera de lectura
        content = file.read()  # variable contenido = texto del archivo que acabo de abrir
        text.delete(1.0, "end")  # borro el texto actual para insertar el del archivo abierto (que he leido)
        text.insert("insert", content)  # inserto el contenido que he leido
        file.close()  # cierro archivo
    window.title(url_file + title)


def save_file():
    global url_file
    if url_file != "":  # Es un archivo ya existente, ya tiene url: abierto -> editado -> guardado
        content = text.get(1.0, "end-1c")  # contenido copia el valor de lo que esta en la caja de texto
        file = open(url_file, "w+")  # w es decir de escritura
        file.write(content)  # que escriba el contendido
        window.title("Archivo Guardado" + url_file + title)
        file.close()
    else:  # Si es un archivo nuevo, que no tiene urlGuardar archivo nuevo
        file = filedialog.asksaveasfile(title="Guardar", mode="w",
                                        defaultextension=".txt")  # ask save a file(Pedir guardar como archivo)
        if file is not None:  # Si archivo no esta vacio
            url_file = file.name
            content = text.get(1.0, "end-1c")
            file = open(url_file, "w+")
            file.write(content)
            window.title("Archivo guardado" + url_file + title)
            file.close()
        else:
            url_file = ""
            window.title("Guardado cancelado" + url_file + title)

def save_as_file():
    global url_file
    file = filedialog.asksaveasfile(title="Guardar Como", mode="w",
                                    defaultextension=".txt")  # ask save a file(Pedir guardar como archivo)
    if file is not None:  # Si archivo no esta vacio
        url_file = file.name
        content = text.get(1.0, "end-1c")
        file = open(url_file, "w+")
        file.write(content)
        window.title("Archivo guardado" + url_file + title)
        file.close()

def limpiarErrores():
    error.config(text="")
    global errores
    errores = ""

def leerLineasInput():
    limpiarErrores()
    content = text.get(1.0, "end-1c")
    lista = content.split('\n')
    contador = 1
    for linea in lista:
        analizarLinea(linea, contador)
        contador = contador + 1 

# luispa:=123
# diego:=111
# ale

def analizarLinea(linea, numeroDeLinea):
    global errores
    estado= 1
    lineaIndex = str(numeroDeLinea)
    for ind, let in enumerate(linea):
        index = str(ind)
        letra = str(let)

        if estado == 1:
            print(letra.isalpha(), letra == ":", letra.isnumeric())
            if letra.isalpha(): # es letra
                estado = 2
            elif letra == ":": # es :
                estado = 3
            
            elif letra.isnumeric(): # es numero
                estado = 5
            else: 
                err = "Linea " + lineaIndex + ", posicion " + index + ": " + "Error de estado inicial, no es numero ni letra ni este simbolo \":\" . Se encontro un '" + letra + "'.\n"
                print(err)
                errores = errores + err
            continue

        if estado == 2:
            if letra.isalpha(): # es letra
                estado = 2
            if letra.isnumeric(): # es :
                estado = 2
            if estado != 2: # si el estado no cambio a 2, hay un error de asignacion
                err = "Linea " + lineaIndex + ", posicion " + index + ": " + "Error de estado secundario, no es ni letra ni numero. Se encontro un '" + letra + "'.\n"
                print(err)
                errores = errores + err
            continue
        
        if estado == 3:
            print(letra)
            if letra != '=': # es signo igual
                err = "Linea " + lineaIndex + ", posicion " + index + ": " + "Se esperaba un =, pero se encontro un '" +  letra + "'.\n"
                print(err)
                errores = errores + err
            continue

        if estado == 4:
            if letra != None: # nil o null equivalente en Python
                err = "Linea " + lineaIndex + ", posicion " + index + ": " + "Se esperaba un valor null, pero se encontró un '" + letra + "'\n"
                print(err)
                errores = errores + err
            continue

        if estado == 5:
            if letra.isnumeric() ==  False: #Si el valor no es un numero 
                err = "Linea " + lineaIndex + ", posicion " + index + ": " + "Se esperaba un valor numerico, pero se encontro un '" + letra + "'\n"
                print(err)
                errores = errores + err
            continue

    print("estado", estado)
    if estado == 1 or estado == 3:
        err = "Linea " + lineaIndex + ": La entrada no es una asignacion válida, no se ha completado la asignacion esperada nombre:=valor.\n"
        print(err)
        errores = errores + err

    if errores != "":
        error.config(text=errores) 
    else:
        error.config(text="Ok")


# separar cada fila del textbox como un stirng
# hacer una funcion que valide los estados del diagrama
# hacer que cada fila se valide y aparezca une error en la pantalla de errores

menu = Menu(window)
new_item = Menu(menu, tearoff=0)

# Elementos dentro del menu desplegable
new_item.add_command(label="Nuevo", command=new_file)
new_item.add_separator()
new_item.add_command(label="Abrir", command=open_file)
new_item.add_separator()
new_item.add_command(label="Guardar", command=save_file)
new_item.add_separator()
new_item.add_command(label="Guardar como", command=save_as_file)
new_item.add_separator()
new_item.add_command(label="Salir", command=window.quit)

# menu desplegable
menu.add_cascade(label="Archivo", menu=new_item)

# imagenNuevo = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Nuevo.PNG").resize((30,30)))
imagenNuevo = ImageTk.PhotoImage(Image.open(r"/Users/admin/repo/python-notepad-final/iconos/nuevo.png").resize((30,30))) # TEMPORAL
botonNuevo = Button(window, command=new_file, image=imagenNuevo)
botonNuevo.pack()
#botonNuevo.grid(column=1, row=0)

# imagenAbrir = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Abrir.png").resize((30,30)))
imagenAbrir = ImageTk.PhotoImage(Image.open(r"/Users/admin/repo/python-notepad-final/iconos/abrir.png").resize((30,30))) # TEMPORAL
botonAbrir = Button(window,command=open_file, image=imagenAbrir)
botonAbrir.pack()
#botonAbrir.grid(column=2, row=0)

# imagenGuardar = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Guardar.png").resize((30,30)))
imagenGuardar = ImageTk.PhotoImage(Image.open(r"/Users/admin/repo/python-notepad-final/iconos/guardar.png").resize((30,30)))
botonGuardar = Button(window, command=save_file, image=imagenGuardar)
botonGuardar.pack()
#botonGuardar.grid(column=3, row=0)

# imagenGuardarComo = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Guardar_como.png").resize((30,30)))
imagenGuardarComo = ImageTk.PhotoImage(Image.open(r"/Users/admin/repo/python-notepad-final/iconos/guardar_como.png").resize((30,30)))
botonGuardarComo = Button(window, command=save_as_file, image=imagenGuardarComo)
botonGuardarComo.pack()
#botonGuardarComo.grid(column=4, row=0)

# imagenAnalizar = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\analizar.png").resize((30,30)))
imagenAnalizar = ImageTk.PhotoImage(Image.open(r"/Users/admin/repo/python-notepad-final/iconos/analizar.png").resize((30,30)))
botonAnalizar = Button(window, command=leerLineasInput, image=imagenAnalizar)
botonAnalizar.pack()
#imagenAnalizar.grid(column=4, row=0)



# Se crea el Text donde se ingresara todo el text
text = Text(window)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=5, )
text.focus()

# Se crea el Text donde se mostraran los errores
error = Label(window, justify=LEFT)
error.pack(fill="both", expand=0)
error.config(bd=0, padx=2, pady=2, )


window.config(menu=menu)
window.mainloop()