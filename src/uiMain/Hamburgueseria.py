import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from src.gestorAplicacion.administracion import *
from src.gestorAplicacion.administracion.Contabilidad import Contabilidad
from src.gestorAplicacion.restaurante import *

# __________________________________________________________________________________________
# Funciones y Eventos
hojas_de_vidas = [
    "Breve biografia de los autores\n \n \n" "Nombre: Nicolas Ruiz Blandon\nFecha de nacimiento: 01/23/04\nGustos: El fercho",
    "Breve biografia de los autores\n \n \n" "Nombre: Juan Felipe Moreno Ruiz\nFecha de nacimiento: 01/22/07\nGustos: El fercho",
    "Breve biografia de los autores\n \n \n" "Nombre: David Delgado Ortiz\nFecha de nacimiento: 01/23/02\nGustos: El fercho",
    "Breve biografia de los autores\n \n \n" "Nombre: Cristian David Pérez Lopera\nFecha de nacimiento: 10/10/05\nGustos: Perros > Gatos. Melómano, & cosas viejas enjoyer.",
    "Breve biografia de los autores\n \n \n" "Nombre: Ivan Dario Gomez Cabrera\nFecha de nacimiento: 01/09/04\nGustos: Le gusta los videojuegos y la música"]
indice_hojas_vida = 0


def cambia_hojas_vida(event):  # Evento para cambiar las hojas de vida al hacer click.
    global indice_hojas_vida
    indice_hojas_vida = (indice_hojas_vida + 1) % len(hojas_de_vidas)
    label3_1.config(text=hojas_de_vidas[indice_hojas_vida])
    label1.config(image=fotos[indice_hojas_vida])
    label2.config(image=fotos[indice_hojas_vida])
    label3.config(image=fotos[indice_hojas_vida])
    label4.config(image=fotos[indice_hojas_vida])
    label5.config(image=fotos[indice_hojas_vida])

def onEnter(event):# Evento del ratón que al pasar sobre la misma región de la foto se podrán cambiar entre 5 imágenes.
    global imagenes, imagenes_index
    imagenes_index = (imagenes_index + 1) % len(imagenes)
    boton_cambiante.config(image=imagenes[imagenes_index])

def evento():
    pass


def ingreso_al_sistema():
    boton_Ventana_Principal.config(state="disabled")
    ventana_del_usuario = Toplevel(frame2)
    ventana_del_usuario.title("Hamburgueseria las Calvas")
    ventana_del_usuario.geometry("800x600")
    ventana_del_usuario.config(cursor="spider")
    ventana_del_usuario.resizable(width=False, height=False)

    def cerrar_ventana():
        if messagebox.askokcancel("Cerrar", "¿Estás seguro de que quieres cerrar el sistema de 'Las Calvas Burgers'?"):
            habilitar_boton()
            ventana_del_usuario.destroy()

    ventana_del_usuario.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    def habilitar_boton():
        boton_Ventana_Principal.config(state="normal")

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

    # Funcion para deshabilitar el boton de la ventana principal

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


        #------------------CONTABILIDAD-------------------#

    def opcionContabilidad():
        #limpieza de ventana
        limpiarVentana()
        creadorMenu()
        ventana_del_usuario.configure(pady=10)

        #label de titulo y descripcion de la funcionalidad
        tituloLabel = Label(ventana_del_usuario, text="CONTABILIDAD", justify="center", pady=10, font=("Helvetica", 16, "bold"))
        tituloLabel.pack(side="top")
        explicacionLabel = Label(ventana_del_usuario, pady=10, font=("Helvetica", 12),
                                 text="Lleva las estadísticas al día sobre los ingresos y gastos del restaurante, y permite pagar las cuentas pendientes.")
        explicacionLabel.pack(side="top", fill="x")

        #creacion del Frame donde va el formulario de interaccion para la funcionalidad
        frameContabilidad = tk.Frame(ventana_del_usuario, padx=10, pady=10)
        frameContabilidad.config(bd=5, relief="groove")
        frameContabilidad.pack(expand=True)

        #definicion de funcion para el boton pagar
        def botonPagar():
            if comboPagos.get()=="Pagar Servicios":
                Contabilidad.pagarServicios()
                labelSaldo.config(text=f"SALDO: {Contabilidad.saldo}")
                print(Contabilidad.saldo)
                entradaTotalPagos.set(str("PAGO REALIZADO CORRECTAMENTE. Dinero descontado del saldo"))
            elif comboPagos.get()=="Pagar Sueldos":
                entradaTotalPagos.set(str("PAGO REALIZADO CORRECTAMENTE. Dinero descontado del saldo"))
                Contabilidad.pagarSueldos()
                print(Contabilidad.getGastos())

        #definicion de funcion para el cambio de opcion en Combobox de pagos
        def descripPagos(event):
            if comboPagos.get()=="Pagar Servicios":
                labelDescripcion.config(text="Pagar el total del valor de los servicios publicos del restaurante.")
            elif comboPagos.get()=="Pagar Sueldos":
                labelDescripcion.config(text="Pagar el salario a todos los trabajadores del restaurante.")

        #label de Pagos
        labelPagos = tk.Label(frameContabilidad, text="PAGOS", anchor="w", width= 20)
        labelPagos.grid(row = 0, column = 0)
        #entrada Pagos
        entradaTotalPagos = tk.StringVar()
        entryTotalPagos = Entry(frameContabilidad, width= 40, state="disabled", textvariable=entradaTotalPagos)
        entryTotalPagos.grid(row = 1, column = 1, padx=10, pady=10)
        #combobox
        comboPagos = ttk.Combobox(frameContabilidad, state="readonly", values=["Pagar Servicios", "Pagar Sueldos"])
        comboPagos.current(0)
        comboPagos.bind("<<ComboboxSelected>>", descripPagos)
        comboPagos.grid(row = 1, column = 0, padx=10, pady=10)
        #label descriptivo
        labelDescripcion = Label(frameContabilidad, text="Pagar el total del valor de los servicios publicos del restaurante.", width=40, wraplength=200, padx=10)
        labelDescripcion.grid(row=2, column=1)
        #boton
        botonPagar = Button(frameContabilidad, text="Realizar Pago", padx=10, command=botonPagar)
        botonPagar.grid(row=1, column=2)

        #definicion de funcion del boton para calcular estadisticas
        def botonCalcular():
            if comboEstadisticas.get()=="Calcular Gastos":
                entradaEstadisticas.set(str(Contabilidad.getIngresos()))
            elif comboEstadisticas.get()=="Calcular Ingresos":
                entradaEstadisticas.set(str(9))
            elif comboEstadisticas.get()=="Calcular Utilidad":
                entradaEstadisticas.set(str(15))

        #definicion de funcion para el cambio de opcion en el combobox de estadisticas
        def descripEstadisticas(event):
            if comboEstadisticas.get()=="Calcular Gastos":
                labelDescripcion2.config(text="Calcula el total de gastos en el mantenimiento del restaurante.")
            elif comboEstadisticas.get()=="Calcular Ingresos":
                labelDescripcion2.config(text="Calcula los ingresos por ventas que registra el restaurante.")
            elif comboEstadisticas.get()=="Calcular Utilidad":
                labelDescripcion2.config(text="Calcula las ganancias netas que obtiene el restaurante según sus costos e ingresos.")

        #label Estadisticas
        labelEstadisticas = tk.Label(frameContabilidad, text="ESTADISTICAS", anchor="w", width= 20)
        labelEstadisticas.grid(row = 3, column = 0)
        #Entry
        entradaEstadisticas = tk.StringVar()
        entryEstadisticas = Entry(frameContabilidad, width= 40, state="disabled", textvariable=entradaEstadisticas)
        entryEstadisticas.grid(row = 4, column = 1, padx=10, pady=10)
        #Combobox
        comboEstadisticas = ttk.Combobox(frameContabilidad, state="readonly", values=["Calcular Ingresos", "Calcular Gastos", "Calcular Utilidad"])
        comboEstadisticas.current(0)
        comboEstadisticas.bind("<<ComboboxSelected>>", descripEstadisticas)
        comboEstadisticas.grid(row = 4, column = 0, padx=10, pady=10)
        #label descriptivo
        labelDescripcion2 = Label(frameContabilidad, text="Calcula los ingresos por ventas que registra el restaurante.", width=40, wraplength=200, padx=10)
        labelDescripcion2.grid(row=5, column=1)
        #boton
        botonCalcular = Button(frameContabilidad, text="Calcular", padx=10, command=botonCalcular)
        botonCalcular.grid(row=4, column=2)

        #Label que muestra el saldo en la parte inferior derecha
        labelSaldo = Label(frameContabilidad,text=f"SALDO {Contabilidad.saldo}", width=20, wraplength=150, font=("Helvetica", 12, "bold"), padx=10, pady=15)
        labelSaldo.grid(row=7, column=2)


    # ===================================================================================================#

    
    def cerrar_ventana():
        if messagebox.askokcancel("Cerrar", "¿Estás seguro de que quieres cerrar el sistema de 'Las Calvas Burgers'?"):
            habilitar_boton()
            ventana_del_usuario.destroy()

    def creadorMenu():
        menuBar = tk.Menu(ventana_del_usuario)
        ventana_del_usuario.config(menu=menuBar)
        archivoMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Archivo", menu=archivoMenu)
        archivoMenu.add_command(label="Aplicación", command=informacion_basica)
        archivoMenu.add_command(label="Salir", command=cerrar_ventana)
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
        informacion = messagebox.showinfo("Nombres de los creadores", "Nicolás Ruiz Blandón" + "\n" +
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


def descripcion():  # Descripción del sistema (con esta aparecerá en un messagebox una breve descripción de lo que hace el sistema)
    texto = messagebox.showinfo("descripción del sistema", "El sistema administrarivo de 'Las Calvas' es un programa integral diseñado para optimizar la gestión de la hamburguesería 'Las Calvas'." + "\n" + "Desde la contabilidad hasta la gestión de personal y la toma de pedidos, automatiza procesos clave para una operación eficiente. Proporciona información financiera precisa, facilita la programación de empleados y agiliza la toma de pedidos, mejorando la experiencia global en Las Calvas")


# __________________________________________________________________________________
ventana = tk.Tk()
ventana.title("Hamburgueseria")
ventana.geometry("1280x600")
ventana.config(cursor="pirate")

menuInicial = tk.Menu(ventana)
ventana.config(menu=menuInicial)
menu1 = tk.Menu(menuInicial, tearoff=0)
menuInicial.add_cascade(label="Inicio", menu=menu1, command=evento)
menu1.add_command(label="Descripción del Sistema", command=descripcion)
menu1.add_command(label="Salir de la Aplicación", command=salir_sistema)
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

imagenes = [PhotoImage(file='carnes1.ppm'), PhotoImage(file='Hamburguesa1.ppm'), PhotoImage(file='Burger_one.ppm'), PhotoImage(file='3.ppm'), PhotoImage(file='2.ppm')] # lista de fotos
imagenes_index = 0  # índice de la foto actual
boton_cambiante = Button(frame2, image=imagenes[imagenes_index])
boton_cambiante.pack()
boton_cambiante.bind('<Enter>',  onEnter)


boton_Ventana_Principal = tk.Button(frame2, text="Ingresar al Sistema",
                                    command=ingreso_al_sistema)  # Permite ingresar a la Ventana de Usuario
boton_Ventana_Principal.pack(side="bottom", anchor="s")

frame1.pack(side="top", fill="both", padx=10, pady=10)
frame1.config(bd=4, relief="groove")
frame2.pack(side="bottom", fill="both", padx=10, pady=10)
frame2.config(bd=4, relief="groove")
# ____________________________________________________________________________

## contenedor 2
frame_principal2 = tk.Frame(ventana, bg="white")
frame_principal2.config(bd=5, relief="groove")
frame_principal2.pack(side="right", fill="both")
frame3 = tk.Frame(frame_principal2, bg="green")  # P5
frame3.pack(side="top", fill="both", padx=10, pady=10)
frame3.config(bd=4, relief="groove")
label3_1 = tk.Label(frame3, text=hojas_de_vidas[indice_hojas_vida], width=50, height=10)# Label asociado al evento de mouse al pasar sobre las imagenes.
label3_1.grid(row=0, column=0, padx=50, pady=0)
label3_1.bind("<Button-1>", cambia_hojas_vida)
label3_1.config(font=("Helvetica", 12, "bold"))

frame4 = tk.Frame(frame_principal2, bg="yellow")  # P6
frame4.pack(side="bottom", fill="both", padx=10, pady=10)
frame4.config(bd=4, relief="groove")

for i in range(2):
    frame4.grid_rowconfigure(i, weight=1)
    frame4.grid_columnconfigure(i, weight=1)

# Crear el objeto PhotoImage con cada imagen
imagen1 = tk.PhotoImage(file="1.png")
imagen2 = tk.PhotoImage(file="2.png")
imagen3 = tk.PhotoImage(file="3.png")
imagen4 = tk.PhotoImage(file="4.png")
imagen5 = tk.PhotoImage(file="1.png")# Reemplaza esto con la ruta a tu imagen

fotos = [imagen1, imagen2, imagen3, imagen4, imagen5]# necesaria para poder vincular las imagenes con la funcion cambia_hojas_vida

# Crear el widget Label con cada imagen y añadirlo al Frame 4
label1 = tk.Label(frame4, image=imagen1)
label2 = tk.Label(frame4, image=imagen2)
label3 = tk.Label(frame4, image=imagen3)
label4 = tk.Label(frame4, image=imagen4)
label5 = tk.Label(frame4, image=imagen5)

label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=0, column=1, sticky="nsew")
label3.grid(row=1, column=0, sticky="nsew")
label4.grid(row=1, column=1, sticky="nsew")
label5.grid(row=0, column=0, sticky="nsew")

ventana.mainloop()
