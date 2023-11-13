import tkinter as tk
from tkinter import *
from tkinter import messagebox
#__________________________________________________________________________________________
#Funciones y Eventos
def evento():
    pass
def ingreso_al_sistema():

    boton_Ventana_Principal.config(state="disabled")
    ventana_del_usuario= Toplevel(frame2)
    ventana_del_usuario.title("Hamburgueseria las Calvas")
    ventana_del_usuario.geometry("1280x600")
    ventana_del_usuario.config(cursor="spider")
    ventana_del_usuario.resizable(width=False, height=False)
    def informacion_basica():
        informacion = messagebox.showinfo("Información de la Apliación", "Esta plataforma integral de gestión para un restaurante de hambueguesas facilita el seguimiento de información clave de empleados. Además, ofrece un servicio de reserva de mesas para garantizar la comodidad de los clientes. Simplifica el proceso de pedidos, facturación y lleva un control eficiente de la contabilidad y el inventario del restaurante, mejorando la eficiencia operativa. ")

    menuBar = tk.Menu(ventana_del_usuario)
    ventana_del_usuario.config(menu=menuBar)
    archivoMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Archivo", menu=archivoMenu)
    archivoMenu.add_command(label="Aplicación", command=informacion_basica)
    archivoMenu.add_command(label="Salir", command = ventana_del_usuario.destroy)
    pycMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Procesos y Consultas", menu=pycMenu)
    pycMenu.add_command(label="Toma de Pedidos")
    pycMenu.add_command(label="Gestion de Reservas")
    pycMenu.add_command(label="Gestion de Empleados")
    pycMenu.add_command(label="Gestion de Inventario")
    pycMenu.add_command(label="Contabilidad")
    ayudaMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Aplicación", menu=ayudaMenu)
    def habilitar_boton(event):
        boton_Ventana_Principal.config(state="normal")

        # En la función ingreso_al_sistema
    ventana_del_usuario.bind("<Destroy>", habilitar_boton)
    #Frame Zona1
    frameUser1 = tk.Frame(ventana_del_usuario, bg= "yellow")
    frameUser1.config(bd= 5, relief="groove")
    frameUser1.pack(side="left", fill="both", expand=True)
    labelUser1 = tk.Label(frameUser1, text="Zona 1")
    labelUser1.pack(side="top", anchor="nw")
    labelUser1.config(bd=5, relief="groove")


def salir_sistema(): #Salir de la aplicación
    ventana.destroy()
def descripcion():#Descripción del sistema (con esta aparecerá en alguna parte de la ventana de inicio una breve descripción de lo que hace el sistema)
    ventana_descripcion = tk.Toplevel(ventana)
    ventana_descripcion.title("Descripción del sistema")
    texto = "El sistema administrarivo de 'Las Calvas' es un programa integral diseñado para optimizar"+"\n"+"la gestión de la hamburguesería 'Las Calvas'. Desde la contabilidad hasta la gestión de "+"\n"+"personal y la toma de pedidos, automatiza procesos clave para una operación eficiente. "+"\n"+"Proporciona información financiera precisa, facilita la programación de empleados y agiliza "+"\n"+"la toma de pedidos, mejorando la experiencia global en Las Calvas"
    label = tk.Label(ventana_descripcion, text=texto)
    ventana_descripcion.resizable(width=False, height=False)
    label = tk.Label(ventana_descripcion, text=texto, font=("Helvetica", 14,"bold"))
    label.pack()
    #label = tk.Label(ventana, text=texto)
    #label.pack()
    #label.place(x=170, y=150)
    #label.config(bd=2, relief="groove")

#__________________________________________________________________________________
ventana = tk.Tk()
ventana.title("Hamburgueseria")
ventana.geometry("1280x600")
ventana.config(cursor="pirate")

menuInicial = tk.Menu(ventana)
ventana.config(menu=menuInicial)
menu1 = tk.Menu(menuInicial)
menuInicial.add_cascade(label="Inicio",menu=menu1,command=evento)
menu1.add_command(label="Salir de la Aplicación",command=salir_sistema)
menu1.add_command(label="Descripción del Sistema",command=descripcion)
ventana.resizable(width=False, height=False)
#__________________________________________________________________________

## contenedor 1
frame_principal1 = tk.Frame(ventana, bg="white")
frame_principal1.place(x=10, y=10, width=5, height=9)
frame_principal1.config(bd=5, relief="groove")

frame_principal1.pack(side="left", fill="both")
frame1 = tk.Frame(frame_principal1, bg="red") #P3
label1 = tk.Label(frame1, text= "¡Bienvenido a Las Calvas, el paraíso de las hamburgesas! 🍔🎉 "+"\n"+"En nuestro rincón gastronómico, cada hamburguesa"+"\n"+" es una obra maestra hecha con amor y sabores inigualables."+"\n"+" Prepárate para un viaje culinario que despierte tus sentidos"+"\n"+" y te haga amar cada bocado. ¡Sumérgete en el sabor "+"\n"+"auténtico de Las Calvas y déjanos conquistar tu paladar"+"\n"+" con nuestras deliciosas creaciones!"+"\n"+" ¡Bienvenido a la experiencia de hamburguesas que siempre soñaste!", font=("Helvetica", 12,"bold"), width=60, wraplength=600)#Brindar un saludo de bienvenida al sistema
label1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky="n")
label1.pack(side="top")
frame2 = tk.Frame(frame_principal1, bg="blue")#P4
boton_Ventana_Principal = tk.Button(frame2, text="Ingresar al Sistema", command= ingreso_al_sistema)# Permite ingresar a la Ventana de Usuario
boton_Ventana_Principal.pack(side="bottom", anchor="s")



frame1.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame1.config(bd=4, relief="groove")
frame2.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)
frame2.config(bd=4, relief="groove")
#____________________________________________________________________________

## contenedor 2
frame_principal2 = tk.Frame(ventana, bg="white")
frame_principal2.config(bd=5, relief="groove")
frame_principal2.pack(side="right", fill="both", expand = True)
frame3 = tk.Frame(frame_principal2, bg="green")#P5
frame4 = tk.Frame(frame_principal2, bg="yellow")#P6

frame3.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame3.config(bd=4, relief="groove")
frame4.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)
frame4.config(bd=4, relief="groove")

#___________________________________________________________________________


ventana.mainloop()
