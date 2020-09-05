from tkinter import *
from tkinter import filedialog
from io import open
from PIL import ImageTk, Image

window = Tk()
title = " Bloc de Notas"
window.title(title)
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
        filetype=(("Archivo de texto", "*.txt"),),
        title="Abrir Archivo")  # con esto ya tenemos la ruta actual del archivo abierto
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
imagenNuevo = ImageTk.PhotoImage(Image.open(r"/home/luispa/Desktop/PR/iconos/nuevo.png").resize((30,30))) # TEMPORAL
botonNuevo = Button(window, command=new_file, image=imagenNuevo)
botonNuevo.pack()
#botonNuevo.grid(column=1, row=0)

# imagenAbrir = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Abrir.png").resize((30,30)))
imagenAbrir = ImageTk.PhotoImage(Image.open(r"/home/luispa/Desktop/PR/iconos/abrir.png").resize((30,30))) # TEMPORAL
botonAbrir = Button(window,command=open_file, image=imagenAbrir)
botonAbrir.pack()
#botonAbrir.grid(column=2, row=0)

# imagenGuardar = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Guardar.png").resize((30,30)))
imagenGuardar = ImageTk.PhotoImage(Image.open(r"/home/luispa/Desktop/PR/iconos/guardar.png").resize((30,30)))
botonGuardar = Button(window, command=save_file, image=imagenGuardar)
botonGuardar.pack()
#botonGuardar.grid(column=3, row=0)

# imagenGuardarComo = ImageTk.PhotoImage(Image.open(r"C:\Users\aleja\Desktop\ImagenesPrograma\Guardar_como.png").resize((30,30)))
imagenGuardarComo = ImageTk.PhotoImage(Image.open(r"/home/luispa/Desktop/PR/iconos/guardar_como.png").resize((30,30)))
botonGuardarComo = Button(window, command=save_as_file, image=imagenGuardarComo)
botonGuardarComo.pack()
#botonGuardarComo.grid(column=4, row=0)



# Se crea el Text donde se ingresara todo el text
text = Text(window)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=5, )
text.focus()


window.config(menu=menu)
window.mainloop()