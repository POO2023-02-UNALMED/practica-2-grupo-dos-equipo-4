import tkinter as tk
from tkinter import *
from tkinter import messagebox

# __________________________________________________________________________________________
# Funciones y Eventos
hojas_de_vidas = ["Nombre: Nicolas Ruiz Blandon\nFecha de nacimiento: 01/23/04\nGustos: El fercho", "Nombre: Juan Felipe Moreno Ruiz\nFecha de nacimiento: 01/22/07\nGustos: El fercho", "Nombre: David Delgado Ortiz\nFecha de nacimiento: 01/23/02\nGustos: El fercho", "Nombre: Cristian David Pérez Lopera\nFecha de nacimiento: 01/23/02\nGustos: El fercho", "Nombre: Ivan Dario Gomez Cabrera\nFecha de nacimiento: 01/09/04\nGustos: El fercho"]
indice_hojas_vida = 0


def cambia_hojas_vida(event):  # Evento para cambiar las hojas de vida al hacer click.
    global indice_hojas_vida
    indice_hojas_vida = (indice_hojas_vida + 1) % len(hojas_de_vidas)
    label3_1.config(text=hojas_de_vidas[indice_hojas_vida])


def evento():
    pass


def ingreso_al_sistema():
    boton_Ventana_Principal.config(state="disabled")
    ventana_del_usuario = Toplevel(frame2)
    ventana_del_usuario.title("Hamburgueseria las Calvas")
    ventana_del_usuario.geometry("1280x600")
    ventana_del_usuario.config(cursor="spider")
    ventana_del_usuario.resizable(width=False, height=False)

# Funcion en la que se crea una messagebox en la que se proporciona información sobre la aplicación
    def informacion_basica():
        informacion = messagebox.showinfo("Información de la Aplicación",
                                          "Esta plataforma integral de gestión para un restaurante de hambueguesas facilita "
                                          "el seguimiento de información clave de empleados. Además, ofrece un servicio de reserva "
                                          "de mesas para garantizar la comodidad de los clientes. Simplifica el proceso de pedidos, "
                                          "facturación y lleva un control eficiente de la contabilidad y el inventario del restaurante, "
                                          "mejorando la eficiencia operativa. ")

    # Funcion para limpiar los widgets de la ventana
    def limpiarVentana():
        for widget in ventana_del_usuario.winfo_children():
            widget.destroy()

    #Funcion para deshabilitar el boton de la ventana principal
    def habilitar_boton(event):
        boton_Ventana_Principal.config(state="normal")
    # En la función ingreso_al_sistema
        ventana_del_usuario.bind("<Destroy>", habilitar_boton)



    # ====================Creador de pestañas de Funcionalidades==========================================#

    def opcionGestionReserva():
        limpiarVentana()
        creadorMenu()
        frameMesas = tk.Frame(ventana_del_usuario, bg="red")
        frameMesas.config(bd=5, relief="groove")
        frameMesas.pack(side="left", fill="both", expand=True)
        labelMesas = tk.Label(frameMesas, text="Gestion de Reservas")
        labelMesas.pack(side="top", anchor="nw")
        labelMesas.config(bd=5, relief="groove")

    def opcionTomaDePedidos():
        limpiarVentana()
        creadorMenu()
        frameMesas = tk.Frame(ventana_del_usuario, bg="red")
        frameMesas.config(bd=5, relief="groove")
        frameMesas.pack(side="left", fill="both", expand=True)
        labelMesas = tk.Label(frameMesas, text="Toma de Pedidos")
        labelMesas.pack(side="top", anchor="nw")
        labelMesas.config(bd=5, relief="groove")

    def opcionGestionEmpleados():
        limpiarVentana()
        creadorMenu()
        frameMesas = tk.Frame(ventana_del_usuario, bg="red")
        frameMesas.config(bd=5, relief="groove")
        frameMesas.pack(side="left", fill="both", expand=True)
        labelMesas = tk.Label(frameMesas, text="Gestion de Empleados")
        labelMesas.pack(side="top", anchor="nw")
        labelMesas.config(bd=5, relief="groove")

    def opcionGestionDeInventario():
        limpiarVentana()
        creadorMenu()
        frameMesas = tk.Frame(ventana_del_usuario, bg="red")
        frameMesas.config(bd=5, relief="groove")
        frameMesas.pack(side="left", fill="both", expand=True)
        labelMesas = tk.Label(frameMesas, text="Gestion de Inventario")
        labelMesas.pack(side="top", anchor="nw")
        labelMesas.config(bd=5, relief="groove")

    def opcionContabilidad():
        limpiarVentana()
        creadorMenu()
        frameMesas = tk.Frame(ventana_del_usuario, bg="red")
        frameMesas.config(bd=5, relief="groove")
        frameMesas.pack(side="left", fill="both", expand=True)
        labelMesas = tk.Label(frameMesas, text="Contabilidad")
        labelMesas.pack(side="top", anchor="nw")
        labelMesas.config(bd=5, relief="groove")

    # ===================================================================================================#

    def creadorMenu():
        menuBar = tk.Menu(ventana_del_usuario)
        ventana_del_usuario.config(menu=menuBar)
        archivoMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Archivo", menu=archivoMenu)
        archivoMenu.add_command(label="Aplicación", command=informacion_basica)
        archivoMenu.add_command(label="Salir", command=ventana_del_usuario.destroy)
        pycMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Procesos y Consultas", menu=pycMenu)
        pycMenu.add_command(label="Toma de Pedidos", command=opcionTomaDePedidos)
        pycMenu.add_command(label="Gestion de Reservas", command=opcionGestionReserva)
        pycMenu.add_command(label="Gestion de Empleados", command=opcionGestionEmpleados)
        pycMenu.add_command(label="Gestion de Inventario", command=opcionGestionDeInventario)
        pycMenu.add_command(label="Contabilidad", command=opcionContabilidad)
        ayudaMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Ayuda", menu=ayudaMenu)
        ayudaMenu.add_command(label="Acerca de", command=acercaDe)

    # Funcion que crea una mesaagebox en donde se muestran los nombres de los integrantes del grupo
    def acercaDe():
        def informacion_basica():
            informacion = messagebox.showinfo("Nicolás Ruiz Blandón" + "\n" +
                                              "Juan Felipe Moreno Ruiz" + "\n" +
                                              "David Delgado Ortiz" + "\n" +
                                              "Cristian David Pérez Lopera" + "\n" +
                                              "Ivan Dario Gomez Cabrera")
    creadorMenu()
    # Frame Zona1
    frameUser1 = tk.Frame(ventana_del_usuario, bg="yellow")
    frameUser1.config(bd=5, relief="groove")
    frameUser1.pack(side="left", fill="both", expand=True)
    labelUser1 = tk.Label(frameUser1, text="Zona 1")
    labelUser1.pack(side="top", anchor="nw")
    labelUser1.config(bd=5, relief="groove")


def salir_sistema():  # Salir de la aplicación
    ventana.destroy()


def descripcion():  # Descripción del sistema (con esta aparecerá en alguna parte de la ventana de inicio una breve descripción de lo que hace el sistema)
    ventana_descripcion = tk.Toplevel(ventana)
    ventana_descripcion.title("Descripción del sistema")
    texto = ("El sistema administrarivo de 'Las Calvas' es un programa integral diseñado para optimizar" + "\n" +
             "la gestión de la hamburguesería 'Las Calvas'. Desde la contabilidad hasta la gestión de " + "\n" +
             "personal y la toma de pedidos, automatiza procesos clave para una operación eficiente. " + "\n" +
             "Proporciona información financiera precisa, facilita la programación de empleados y agiliza " + "\n" +
             "la toma de pedidos, mejorando la experiencia global en Las Calvas")
    label = tk.Label(ventana_descripcion, text=texto)
    ventana_descripcion.resizable(width=False, height=False)
    label = tk.Label(ventana_descripcion, text=texto, font=("Helvetica", 14, "bold"))
    label.pack()
    # label = tk.Label(ventana, text=texto)
    # label.pack()
    # label.place(x=170, y=150)
    # label.config(bd=2, relief="groove")


# __________________________________________________________________________________
ventana = tk.Tk()
ventana.title("Hamburgueseria")
ventana.geometry("1280x600")
ventana.config(cursor="pirate")

menuInicial = tk.Menu(ventana)
ventana.config(menu=menuInicial)
menu1 = tk.Menu(menuInicial, tearoff=0)
menuInicial.add_cascade(label="Inicio", menu=menu1, command=evento)
menu1.add_command(label="Salir de la Aplicación", command=salir_sistema)
menu1.add_command(label="Descripción del Sistema", command=descripcion)
ventana.resizable(width=False, height=False)
# __________________________________________________________________________

## contenedor 1
frame_principal1 = tk.Frame(ventana, bg="white")
frame_principal1.place(x=10, y=10, width=5, height=9)
frame_principal1.config(bd=5, relief="groove")

frame_principal1.pack(side="left", fill="both")
frame1 = tk.Frame(frame_principal1, bg="red")  # P3
label1 = tk.Label(frame1,
                  text="¡Bienvenido a Las Calvas, el paraíso de las hamburguesas! 🍔🎉 " + "\n" +
                       "En nuestro rincón gastronómico, cada hamburguesa" + "\n" +
                       " es una obra maestra hecha con amor y sabores inigualables." + "\n" +
                       " Prepárate para un viaje culinario que despierte tus sentidos" + "\n" +
                       " y te haga amar cada bocado. ¡Sumérgete en el sabor " + "\n" +
                       "auténtico de Las Calvas y déjanos conquistar tu paladar" + "\n" +
                       " con nuestras deliciosas creaciones!" + "\n" +
                       " ¡Bienvenido a la experiencia de hamburguesas que siempre soñaste!",
                  font=("Helvetica", 12, "bold"), width=60,
                  wraplength=600)  # Brindar un saludo de bienvenida al sistema
label1.grid(row=0, column=0, padx=10, pady=10, sticky="n")
label1.pack(side="top")
frame2 = tk.Frame(frame_principal1, bg="blue")  # P4
boton_Ventana_Principal = tk.Button(frame2, text="Ingresar al Sistema",
                                    command=ingreso_al_sistema)  # Permite ingresar a la Ventana de Usuario
boton_Ventana_Principal.pack(side="bottom", anchor="s")

frame1.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame1.config(bd=4, relief="groove")
frame2.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)
frame2.config(bd=4, relief="groove")
# ____________________________________________________________________________

## contenedor 2
frame_principal2 = tk.Frame(ventana, bg="white")
frame_principal2.config(bd=5, relief="groove")
frame_principal2.pack(side="right", fill="both", expand=True)
frame3 = tk.Frame(frame_principal2, bg="green")  # P5
frame3.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame3.config(bd=4, relief="groove")
label3_1 = tk.Label(frame3, text=hojas_de_vidas[indice_hojas_vida], width=30, height=10)
label3_1.grid(row=0, column=0, padx=150, pady=0)
label3_1.bind("<Button-1>", cambia_hojas_vida)
label3_1.config(font=("Helvetica", 12, "bold"))

frame4 = tk.Frame(frame_principal2, bg="yellow")  # P6
frame4.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)
frame4.config(bd=4, relief="groove")

'''
# Crear el objeto PhotoImage con cada imagen
imagen1 = tk.PhotoImage(file="src/baseDatos/temp/Image/4.png")  # Reemplaza esto con la ruta a tu imagen
imagen2 = tk.PhotoImage(file="src/baseDatos/temp/Image/Burger one.png")  # Reemplaza esto con la ruta a tu imagen
imagen3 = tk.PhotoImage(file="src/baseDatos/temp/Image/image 2.png")  # Reemplaza esto con la ruta a tu imagen
imagen4 = tk.PhotoImage(file="src/baseDatos/temp/Image/image 3.png")  # Reemplaza esto con la ruta a tu imagen

# Crear el widget Label con cada imagen y añadirlo al Frame 4
label1 = tk.Label(frame4, image=imagen1)
label2 = tk.Label(frame4, image=imagen2)
label3 = tk.Label(frame4, image=imagen3)
label4 = tk.Label(frame4, image=imagen4)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)
'''
# ___________________________________________________________________________


ventana.mainloop()
