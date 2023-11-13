import tkinter as tk
from tkinter import *
#__________________________________________________________________________________________
#Funciones y Eventos
def evento():
    pass
def ingreso_al_sistema():
    ventana_del_usuario= Toplevel(frame2)
    ventana_del_usuario.title("Hamburgueseria las Calvas")
    ventana_del_usuario.geometry("800x600")
    ventana_del_usuario.config(cursor="spider")
    ventana_del_usuario.resizable(width=False, height=False)
    frame0 = tk.Frame(ventana_del_usuario, bg= "yellow")
    frame0.config(bd= 5, relief="groove")
    frame0.pack(side="left", fill="both", expand=True)
    label0 = tk.Label(frame0, text="Las Calvas, Zona 0")
    label0.pack(side="top", anchor="nw")
    label0.config(bd=5, relief="groove")
    frame0_1 = tk.Frame(frame0, bg="blue")
    frame0_1.config(bd=5, relief="groove")
    frame0_1.pack(side="top", fill="both", padx=10, pady=10, expand=True)
    label0_1 = tk.Label(frame0_1, text="Zona 1")
    label0_1.pack(side="top", anchor="nw")
    label0_1.config(bd=5, relief="groove")

    menuBar = tk.Menu(ventana_del_usuario)
    ventana_del_usuario.config(menu=menuBar)
    adminMenu = tk.Menu(menuBar, tearoff=0)
    adminMenu.add_command(label="Empleados")
    menuBar.add_cascade(label="Administracion", menu=adminMenu)
    restaurantMenu = tk.Menu(menuBar, tearoff=0)
    restaurantMenu.add_command(label="Inventario")
    menuBar.add_cascade(label="Restaurante", menu=restaurantMenu)
     

    frame0_2 = tk.Frame(frame0_1, bg= "red")
    frame0_2.config(bd=5, relief="groove")
    frame0_2.pack(side="left", fill="both", expand=True)
    label0_2 = tk.Label(frame0_2, text="Zona 2")
    label0_2.pack(side="bottom", anchor="se")
    label0_2.config(bd=5, relief="groove")



def salir_sistema(): #Salir de la aplicación
    ventana.destroy()
def descripcion():#Descripción del sistema (con esta aparecerá en alguna parte de la ventana de inicio una breve descripción de lo que hace el sistema)
    ventana_descripcion = tk.Toplevel(ventana)
    ventana_descripcion.title("Descripción del sistema")
    texto = "El sistema administrarivo de Las Calvas es un programa integral diseñado para optimizar"+"\n"+"la gestión de la hamburguesería Las Calvas. Desde la contabilidad hasta la gestión de "+"\n"+"personal y la toma de pedidos, automatiza procesos clave para una operación eficiente. "+"\n"+"Proporciona información financiera precisa, facilita la programación de empleados y agiliza "+"\n"+"la toma de pedidos, mejorando la experiencia global en Las Calvas"
    label = tk.Label(ventana_descripcion, text=texto)
    label.pack()

    #label = tk.Label(ventana, text=texto)
    #label.pack()
    #label.place(x=170, y=150)
    #label.config(bd=2, relief="groove")

#__________________________________________________________________________________
ventana = tk.Tk()
ventana.title("Hamburgueseria")
ventana.geometry("800x600")
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
frame_principal1.pack(padx=10, pady=10, ipadx=2, ipady=3)
frame_principal1.config(bd=5, relief="groove")

frame_principal1.pack(side="left", fill="both", expand=True)
frame1 = tk.Frame(frame_principal1, bg="red") #P3
label1 = tk.Label(frame1, text= "¡Bienvenido a Las Calvas, el paraíso de las hamburgesas! 🍔🎉 "+"\n"+"En nuestro rincón gastronómico, cada hamburguesa"+"\n"+" es una obra maestra hecha con amor y sabores inigualables."+"\n"+" Prepárate para un viaje culinario que despierte tus sentidos"+"\n"+" y te haga amar cada bocado. ¡Sumérgete en el sabor "+"\n"+"auténtico de Las Calvas y déjanos conquistar tu paladar"+"\n"+" con nuestras deliciosas creaciones!"+"\n"+" ¡Bienvenido a la experiencia de hamburguesas que siempre soñaste!", font=("Helvetica", 12,"bold"))#Brindar un saludo de bienvenida al sistema
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
frame_principal2.pack(side="right", fill="both", expand=True)
frame3 = tk.Frame(frame_principal2, bg="green")#P5
frame4 = tk.Frame(frame_principal2, bg="yellow")#P6

frame3.pack(side="top", fill="both", padx=10, pady=10, expand=True)
frame3.config(bd=4, relief="groove")
frame4.pack(side="bottom", fill="both", padx=10, pady=10, expand=True)
frame4.config(bd=4, relief="groove")

#___________________________________________________________________________


ventana.mainloop()
